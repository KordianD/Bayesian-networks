from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from mma import net_setup, get_result, get_all_posteriors, change_evidence_and_update, print_all_posteriors
from utils import split, get_offsets
from ui import WrappedButton
from functools import partial


sm = ScreenManager(transition=SwapTransition())
net = net_setup()
net.update_beliefs()


class QuestionsScreen(Screen):

    def __init__(self, **kwargs):
        super(QuestionsScreen, self).__init__(**kwargs)
        self.floater = FloatLayout()
        self.result = None
        self.data = get_all_posteriors(net)
        self.button_answers = {}
        self.apply_nodes_to_labels()

        self.add_widget(self.floater)

    def apply_nodes_to_labels(self):
        nodes = list(self.data.keys())
        result_node = [nodes[-1]]
        nodes_up, nodes_down = split(nodes[:-1])
        self.apply_labels_to_floater(nodes_up, 0.9)
        self.apply_labels_to_floater(nodes_down, 0.6)
        self.apply_labels_to_floater(result_node, 0.23, False)

    def apply_labels_to_floater(self, nodes, y_offset, with_answers=True):
        nodes_count = len(nodes)
        button_size, space_between_buttons = get_offsets(nodes_count)
        for idx, node_name in enumerate(nodes):
            x_offset = (space_between_buttons + button_size / 2) + idx * (space_between_buttons + button_size)
            label = Label(
                text=node_name,
                size_hint=(button_size, 0.05),
                pos_hint={
                    'center_x': x_offset,
                    'center_y': y_offset},
                halign='center')
            self.floater.add_widget(label)
            if with_answers:
                self.apply_buttons_to_floater(node_name, x_offset, y_offset)
            else:
                self.apply_result_floater()

    def apply_buttons_to_floater(self, node, x_offset, y_offset):
        self.button_answers[node] = {}
        for idx, answer in enumerate(self.data[node].keys()):
            button = WrappedButton(
                text=answer,
                size_hint=(0.2, 0.05),
                pos_hint={
                    'center_x': x_offset,
                    'center_y': y_offset - (idx + 1) * 0.05},
                halign='center')
            button_callback = partial(self.answer_the_question, node)
            button.bind(on_press=button_callback)
            self.floater.add_widget(button)
            self.button_answers[node][answer] = button

    def apply_result_floater(self):
        self.result = Label(
            text='',
            font_size='50sp',
            size_hint=(0.2, 0.1),
            pos_hint={
                'center_x': 0.55,
                'center_y': 0.1},
            halign='center')
        self.floater.add_widget(self.result)

    def answer_the_question(self, question, instance):
        checked = self.button_answers[question][instance.text].checked
        answer = None if checked else instance.text
        change_evidence_and_update(net, question, answer)
        print_all_posteriors(net)
        self.result.text = f'{int(get_result(net) * 100)} %'

        for button_name in self.button_answers[question]:
            self.button_answers[question][button_name].color = [1, 1, 1, 1]
            self.button_answers[question][button_name].checked = False

        if not checked:
            self.button_answers[question][instance.text].color = [40, 100, 30, 1]
            self.button_answers[question][instance.text].checked = True


class MMAApp(App):

    def build(self):
        sm.add_widget(QuestionsScreen(name="questions"))
        return sm


if __name__ == '__main__':
    MMAApp().run()
