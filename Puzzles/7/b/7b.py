from operator import itemgetter

steps = {}
executed_steps = []
executing_steps = []
seconds_elapsed = 0
workers_available = 5

def create_step_for_letter_if_needed(letter):
    if letter not in steps:
        step = {
            "letter": letter,
            "dependencies": [],
            "seconds_to_complete": seconds_to_complete_letter(letter)
        }
        steps[letter] = step

def step_for_letter(letter):
    step = steps[letter]
    return step

def step_is_ready(step):
    dependencies = step["dependencies"]
    step_is_ready = (len(dependencies) == 0)
    return step_is_ready

def ready_steps():
    ready_steps = []

    for step in steps.values():
        is_ready = step_is_ready(step)
        if is_ready:
            ready_steps.append(step)
    
    return ready_steps

def first_ready_step():
    sorted_steps = sorted(ready_steps(), key=itemgetter('letter'))
    first_step = sorted_steps[0]
    return first_step

def execute_step(step):
    
    delete_step_letter_from_dependencies(letter)

    executing_steps.append(step)
    letter = step["letter"]
    del steps[letter]

def delete_step_letter_from_dependencies(letter):
    for step in steps.values():
        dependencies = step["dependencies"]
        if letter in dependencies:
            dependencies.remove(letter)

def executed_letter_string():
    string = ""

    for step in executed_steps:
        letter = step["letter"]
        string = string + letter
    
    return string

def seconds_to_complete_letter(letter):
    difference = ord(letter) - ord("A")
    seconds = 60 + difference + 1
    return seconds

def populate_steps():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    for line in lines:
        subject_step_letter = line[36]
        dependency_step_letter = line[5]
        
        create_step_for_letter_if_needed(subject_step_letter)
        create_step_for_letter_if_needed(dependency_step_letter)
        
        step = step_for_letter(subject_step_letter)
        dependencies = step["dependencies"]
        dependencies.append(dependency_step_letter)
        step["dependencies"] = dependencies
        steps[subject_step_letter] = step

def is_finished():
    no_steps_are_remaining = (len(steps.values()) == 0)
    no_steps_are_executing = (len(executing_steps) == 0)
    is_finished = (no_steps_are_remaining and no_steps_are_executing)
    return is_finished

def can_start_new_work():
    workers_are_available = (workers_available > 0)
    steps_are_ready = len(ready_steps() > 0)
    can_start_new_work = (workers_are_available and steps_are_ready)

def start_new_work():
    workers_available = workers_available - 1
    first_step = first_ready_step()
    execute_step(first_step)

def tick_executing_steps():
    for step in executing_steps:
        seconds_to_complete = step["seconds_to_complete"]
        seconds_to_complete = seconds_to_complete - 1
        step["seconds_to_complete"] = seconds_to_complete

def clean_up_finished_executing_steps():
    for step in executing_steps:
        seconds_to_complete = step["seconds_to_complete"]
        if seconds_to_complete == 0:
            executing_steps.remove(step)
            executed_steps.append(step)

if __name__ == "__main__":
    populate_steps()

    while (is_finished() == False):
        while (can_start_new_work()):
            start_new_work()

    seconds_elapsed = seconds_elapsed + 1

    print("seconds_elapsed: ", seconds_elapsed)
