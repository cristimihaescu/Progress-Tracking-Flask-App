import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']
stories_id_list = []


def read_all_user_story_from_csv():
    with open("data.csv", "r") as file:
        csv_file = csv.DictReader(file)
        return [dict(row) for row in csv_file]


def update_stories_id_list(user_stories):
    stories_id_list.clear()
    for user_story in user_stories:
        stories_id_list.append(int(user_story['id']))


def get_all_user_story():
    user_stories = read_all_user_story_from_csv()
    update_stories_id_list(user_stories)
    return user_stories


def get_new_user_story_id():
    new_story_id = max(stories_id_list) + 1 if stories_id_list else 1
    stories_id_list.append(new_story_id)
    return new_story_id

    
def create_new_user_story(input_data):
    new_story = {key:value for key, value in input_data.items()}
    new_story['id'] = get_new_user_story_id()
    add_new_user_story_to_csv(new_story)


def add_new_user_story_to_csv(new_story):
    with open("data.csv", "a", newline='') as file:
        csv_file = csv.DictWriter(file, fieldnames=DATA_HEADER)
        csv_file.writerow(new_story)


def update_all_user_story_in_csv(user_stories):
    with open("data.csv", 'w', newline='') as file:
        csv_file = csv.DictWriter(file, fieldnames=DATA_HEADER)
        csv_file.writeheader()
        for user_story in user_stories:
            csv_file.writerow(user_story)


def get_specific_user_story(story_id):
    user_stories = get_all_user_story()
    for user_story in user_stories:
        if user_story['id'] == story_id:
            return user_story


def update_user_story(input_data, story_id):
    user_stories = get_all_user_story()
    for user_story in user_stories:
        if user_story['id'] == story_id:
            user_story.update(input_data)
    update_all_user_story_in_csv(user_stories)