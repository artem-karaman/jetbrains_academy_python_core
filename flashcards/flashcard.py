import random

from logger import Logger


class Flashcards:

    def __init__(self, logger: Logger, args):
        self.logger = logger
        self.cards_dict = {}
        self.mistakes_dict = {}
        # start
        self.action = ""
        self.args = args

    def card_term_already_exist(self, term):
        if term in self.cards_dict.keys():
            return True
        return False

    def card_definition_already_exist(self, definition):
        if definition in self.cards_dict.values():
            return True
        return False

    def get_unique_term(self):
        term = ""
        unique_term = False
        while not unique_term:
            term = self.logger.logged_input()
            if self.card_term_already_exist(term):
                self.logger.print_and_log(f'The term "{term}" already exists. Try again:')
            else:
                unique_term = True
        return term

    def get_unique_definition(self):
        definition = ""
        unique_definition = False
        while not unique_definition:
            definition = self.logger.logged_input()
            if self.card_definition_already_exist(definition):
                self.logger.print_and_log(f'The definition "{definition}" already exists. Try again:')
            else:
                unique_definition = True
        return definition

    def action_add(self):
        self.logger.print_and_log("The card")
        cards_term = self.get_unique_term()
        self.logger.print_and_log("The definition of the card:")
        cards_definition = self.get_unique_definition()
        self.cards_dict[cards_term] = cards_definition
        self.logger.print_and_log(f"The pair (\"{cards_term}\":\"{cards_definition}\") has been added.\n")

    def action_ask(self):
        self.logger.print_and_log("How many times to ask?")
        times_to_ask = int(self.logger.logged_input())
        while times_to_ask != 0:
            index = random.randrange(0, len(self.cards_dict.keys()))
            key = list(self.cards_dict.keys())[index]
            value = self.cards_dict[key]
            self.logger.print_and_log(f'Print the definition of "{key}":')
            answer = self.logger.logged_input()
            if answer == self.cards_dict[key]:
                self.logger.print_and_log("Correct!")
                times_to_ask -= 1
            else:
                # save wrong answer
                try:
                    result = self.mistakes_dict[key]
                except BaseException as ex:
                    result = 0
                self.mistakes_dict[key] = result + 1

                right_key = ""

                if answer in self.cards_dict.values():
                    for k, v in self.cards_dict.items():
                        if answer == v:
                            right_key = k
                if right_key != "":
                    self.logger.print_and_log(
                        f'Wrong. The right answer is "{self.cards_dict[key]}", but your definition is correct fo "{right_key}".')
                    times_to_ask -= 1
                else:
                    self.logger.print_and_log(f'Wrong. The right answer is "{self.cards_dict[key]}".')
                    times_to_ask -= 1

    def action_export(self):
        self.logger.print_and_log("File name:")
        file_name = self.logger.logged_input()
        with open(file_name, 'w') as file:
            for k, v in self.cards_dict.items():
                file.write(f"{k},{v}\n")
        self.logger.print_and_log(f"{len(self.cards_dict)} cards have been saved.")

    def export_cards(self):
        with open(self.args.export_to, 'w') as file:
            for k, v in self.cards_dict.items():
                file.write(f"{k},{v}\n")
        self.logger.print_and_log(f"{len(self.cards_dict)} cards have been saved.")

    def action_remove(self):
        self.logger.print_and_log("Which card?")
        card_name = self.logger.logged_input()
        if card_name in self.cards_dict.keys():
            del self.cards_dict[card_name]
            self.logger.print_and_log("The card has been removed.")
        else:
            self.logger.print_and_log(f"Can't remove \"{card_name}\": there is no such card.")

    def import_cards(self):
        with open(self.args.import_from, 'r') as file:
            counter = 0
            for line in file:
                k, v = line.split(',')
                self.cards_dict[k] = str(v).replace('\n', '')
                counter += 1
            self.logger.print_and_log(f"{counter} cards have been loaded.")

    def action_import(self):
        self.logger.print_and_log("File name:")
        file_name = self.logger.logged_input()
        try:
            with open(file_name, 'r') as file:
                counter = 0
                for line in file:
                    k, v = line.split(',')
                    self.cards_dict[k] = str(v).replace('\n', '')
                    counter += 1
                self.logger.print_and_log(f"{counter} cards have been loaded.")
        except Exception:
            self.logger.print_and_log("File not found.")

    def hardest_card_action(self):
        if not self.mistakes_dict:
            self.logger.print_and_log("There are no cards with errors.")
        else:
            self.mistakes_dict = dict(sorted(self.mistakes_dict.items(), key=lambda item: item[1], reverse=True))
            result_dict = {}
            for k, v in self.mistakes_dict.items():
                if v == list(self.mistakes_dict.values())[0]:
                    result_dict[k] = v

            if len(result_dict) == 1:
                k, v = list(result_dict.items())[0]
                self.logger.print_and_log(f'The hardest card is "{k}". You have {v} errors answering it.')
            else:
                keys = ""
                values = ""
                for k in result_dict.keys():
                    keys += f'"{k}"'

                for v in result_dict.values():
                    values += f'{v}'
                self.logger.print_and_log(f'The hardest card is {keys}. You have{values} errors answering it.')

    def reset_action(self):
        self.mistakes_dict = {}
        self.logger.print_and_log('Card statistics have been reset.')

    def start(self):
        while self.action != "exit":

            if self.args.import_from:
                self.import_cards()

            self.logger.print_and_log(
                'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
            action = self.logger.logged_input()

            if action == "add":
                self.action_add()

            if action == "ask":
                self.action_ask()

            if action == "export":
                self.action_export()

            if action == "remove":
                self.action_remove()

            if action == "import":
                self.action_import()

            if action == "log":
                self.logger.save_logs()

            if action == "hardest card":
                self.hardest_card_action()

            if action == "reset stats":
                self.reset_action()

            if action == "exit":
                self.logger.print_and_log('Bye bye!')
                if self.args.export_to:
                    self.export_cards()
                exit()
