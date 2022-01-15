from mycroft import MycroftSkill, intent_file_handler


class MySqliteDatabaseAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.database.sqlite.my.intent')
    def handle_assistant_database_sqlite_my(self, message):
        self.speak_dialog('assistant.database.sqlite.my')


def create_skill():
    return MySqliteDatabaseAssistant()

