import requests
from typing import Dict, List

GROUPS_ADRESS = ""
STUDENTS_ADRESS = ""
SCHEDULE_ADRESS = ""


""" GROUPS """

def get_groups() -> List[Dict]:
    return requests.post(GROUPS_ADRESS + "get/").json()

def get_leaders() -> List[Dict]:
    return [group["leaderId"] for group in get_groups()]


""" STUDENTS """

def get_students() -> List[Dict]:
    return requests.post(STUDENTS_ADRESS + "get/").json()

def get_student(id) -> List[Dict]:
    return requests.post(STUDENTS_ADRESS + "getById/",
        {"studentId": id}
    ).json()

def addStudent(groupId, name, surname):
    return requests.post(STUDENTS_ADRESS + "change/group",
        {
            "groupId": groupId,
            "name": name,
            "surname": surname
        }
    ).json()

def deleteStudent(studentId):
    return requests.post(STUDENTS_ADRESS + "change/group",
        {"studentId": studentId}
    ).json()

def changeGroup(studentId, newGroupId):
    return requests.post(STUDENTS_ADRESS + "change/group",
        {
            "studentId": studentId,
            "groupId": newGroupId
        }
    ).json()


""" SCHEDULE """

def get_schedule() -> List[Dict]:
    return requests.post(SCHEDULE_ADRESS + "get/").json()