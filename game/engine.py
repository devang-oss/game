class StoryNode:
    def __init__(self, id, text, choices=None):
        self.id = id
        self.text = text
        self.choices = choices or []

    def add_choice(self, choice):
        self.choices.append(choice)

class Choice:
    def __init__(self, text, next_node_id):
        self.text = text
        self.next_node_id = next_node_id

class StoryEngine:
    def __init__(self):
        self.nodes = {}
        self.current_node = None

    def add_node(self, node):
        self.nodes[node.id] = node

    def start_story(self, starting_node_id):
        self.current_node = self.nodes.get(starting_node_id)

    def make_choice(self, choice_index):
        if self.current_node and choice_index < len(self.current_node.choices):
            choice = self.current_node.choices[choice_index]
            self.current_node = self.nodes.get(choice.next_node_id)
            return self.current_node
        return None

    def get_current_node_text(self):
        return self.current_node.text if self.current_node else ""

# Example usage of the Story Engine
if __name__ == '__main__':
    engine = StoryEngine()
    node1 = StoryNode(1, "Once upon a time...")
    node2 = StoryNode(2, "In a dark forest...")
    choice1 = Choice("Go into the forest", 2)
    node1.add_choice(choice1)
    engine.add_node(node1)
    engine.add_node(node2)
    engine.start_story(1)
    print(engine.get_current_node_text())  # Outputs the story text of the current node.