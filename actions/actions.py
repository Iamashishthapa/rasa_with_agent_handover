# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class Action_Greet(Action):

    def name(self) -> Text:
        return "action_greet"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(text="Welcome to Aligned Customer Support.")
        dispatcher.utter_message(text="Who would you like to talk to from the Support team:")
        dispatcher.utter_message(text="['Hadi Ismail IT & Security','Faysal Ahmad Technical Support', 'Yaacoub Youssef IT Manager', 'Mohamad Hellani Project Manager']")
        return []


class ActionAssignDepartment(Action):

    def name(self) -> Text:
        return "action_assign_department"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        department = tracker.get_slot('department')
        department = tracker.latest_message['entities'][0]['value']
        print(department)
        # print(tracker.latest_message)
        # print(tracker.latest_message['entities'][0]['value'])
        
        if department == "IT & Security":
            dispatcher.utter_message(text="Someone from the IT & Security department will be with you shortly, estimate waiting time is 30 minutes.")
        elif department.lower() == "Project Manager":
            dispatcher.utter_message(text="Someone from the Project Management department will be with you shortly, estimate waiting time is 20 minutes.")
        elif department.lower() == "Technical Support":
            dispatcher.utter_message(text="Someone from the Technical Support department will be with you shortly, estimate waiting time is 25 minutes.")
        else:
            dispatcher.utter_message(text="I'm sorry, I didn't understand which department you want to talk to. Please choose from IT, Project Manager, or Accounting.")

        return [SlotSet("department", department)]



# class ActionGreet(Action):

#     def name(self) -> Text:
#         return "action_greet"

#     async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Sending a thank you message
#         department = tracker.get_slot('department')
#         if department is None:
#             dispatcher.utter_message(response="utter_greet")
#         else:
#             if department.lower() == "it":
#                 dispatcher.utter_message(text="Someone from the IT department will be with you shortly, estimate waiting time is 30 minutes.")
#             elif department.lower() == "project manager":
#                 dispatcher.utter_message(text="Someone from the Project Management department will be with you shortly, estimate waiting time is 20 minutes.")
#             elif department.lower() == "accounting":
#                 dispatcher.utter_message(text="Someone from the Accounting department will be with you shortly, estimate waiting time is 25 minutes.")
#             else:
#                 dispatcher.utter_message(text="I'm sorry, I didn't understand which department you want to talk to. Please choose from IT, Project Manager, or Accounting.")
#         return []
