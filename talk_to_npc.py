from Dialogue import *
from storyline import *

STORY_TALKED_SAMANTHA_S2 = "SAMANTHA STAGE 2"
STORY_TALKED_SAMANTHA_S4C = "SAMANTHA STAGE 4C"
STORY_TALKED_SAMANTHA_S5C = "SAMANTHA STAGE 5C"
STORY_TALKED_SAMANTHA_S4A = "SAMANTHA STAGE 4A"
STORY_TALKED_JENIFER_S2 = "JENIFER STAGE 2"
STORY_TALKED_JENIFER_S32 = "JENIFER STAGE 32"
STORY_TALKED_JENIFER_S5C = "JENIFER STAGE 5C"
STORY_TALKED_DEBRA_S2 = "DEBRA STAGE 2"
STORY_TALKED_DEBRA_S4C = "DEBRA STAGE 4C"
STORY_TALKED_DEBRA_S5C = "DEBRA STAGE 5C"
STORY_TALKED_ALEXA_S2 = "ALEXA STAGE 2"
STORY_TALKED_ALEXA_S3 = "ALEXA STAGE 3"
STORY_TALKED_ALEXA_S31 = "ALEXA STAGE 31"
STORY_TALKED_ALEXA_S4C = "ALEXA STAGE 4C"
STORY_TALKED_ALEXA_S5C = "ALEXA STAGE 5C"
STORY_TALKED_ALEXA_S4A = "ALEXA STAGE 4A"
STORY_TALKED_BOB_S2 = "BOB STAGE 2"
STORY_TALKED_BOB_S3 = "BOB STAGE 3"
STORY_TALKED_BOB_S4C = "BOB STAGE 4C"
STORY_TALKED_BOB_S5C = "BOB STAGE 5C"
STORY_TALKED_STEPHEN_S5C = "STEPHEN STAGE 5C"

talks_progress = []


def samantha_talks(current_room):
    from player import story_progress
    global talks_progress
    if not stage_2["Completion"]:
        story_progress.append(STORY_TALKED_TO_SAMANTHA)
        talks_progress.append(STORY_TALKED_SAMANTHA_S2)
        print(stage_2["SamanthaStart"])
    elif not stage_3["Completion"] and STORY_TALKED_SAMANTHA_S2 in talks_progress:
        print(stage_2["SamanthaRepeat"])
    elif not stage_3_4["Completion"]:
        print(stage_3["SamanthaRepeat"])
    elif STORY_COFFEE_STARTED in story_progress:
        if not stage_4_2C["Completion"]:
            if not (STORY_TALKED_SAMANTHA_S4C in talks_progress):
                talks_progress.append(STORY_TALKED_SAMANTHA_S4C)
                print(stage_4Coffee["SamanthaStart"])
            elif (STORY_TALKED_SAMANTHA_S4C in talks_progress):
                print(stage_4Coffee["SamanthaRepeat"])
        elif not stage_5Coffee["Completion"]:
            if not (STORY_TALKED_SAMANTHA_S5C in talks_progress):
                talks_progress.append(STORY_TALKED_SAMANTHA_S5C)
                print(stage_5Coffee["SamanthaStart"])
            elif (STORY_TALKED_SAMANTHA_S5C in talks_progress):
                print(stage_5Coffee["SamanthaRepeat"])
        elif not stage_6Coffee["Completion"]:
            print(stage_6Coffee["SamanthaRepeat"])
    elif STORY_DOUBLE_STARTED in story_progress:
        if not stage_4Agent["Completion"]:
            if not (STORY_TALKED_SAMANTHA_S4A in talks_progress):
                talks_progress.append(STORY_TALKED_SAMANTHA_S4A)
                print(stage_4Agent["SamanthaStart"])
            elif (STORY_TALKED_SAMANTHA_S4A in talks_progress):
                print(stage_4Agent["SamanthaRepeat"])
        elif not stage_5Agent["Completion"]:
            print(stage_5Agent["SamanthaRepeat"])


def jenifer_talks(current_room):
    from player import story_progress
    global talks_progress
    if not stage_1["Completion"]:
        print(stage_1["Jenifer"])
    elif not stage_3["Completion"]:
        if not (STORY_TALKED_JENIFER_S2 in talks_progress):
            talks_progress.append(STORY_TALKED_JENIFER_S2)
            print(stage_2["Jenifer"])
        elif (STORY_TALKED_JENIFER_S2 in talks_progress):
            print(stage_2["JeniferRepeat"])
    elif not stage_3_2["Completion"]:
        print(stage_3["JeniferRepeat"])
    elif not stage_3_3["Completion"]:
        if not (STORY_TALKED_JENIFER_S32 in talks_progress):
            talks_progress.append(STORY_TALKED_JENIFER_S32)
            print(stage_3_2["JeniferStart"])
        elif (STORY_TALKED_JENIFER_S32 in talks_progress):
            print(stage_3_2["JeniferRepeat"])
    elif STORY_COFFEE_STARTED in story_progress:
        if not stage_4_2C["Completion"]:
            print(stage_4Coffee["JeniferRepeat"])
        elif not stage_5Coffee["Completion"]:
            if not (STORY_TALKED_JENIFER_S5C in talks_progress):
                talks_progress.append(STORY_TALKED_JENIFER_S5C)
                print(stage_5Coffee["JeniferStart"])
            elif (STORY_TALKED_JENIFER_S5C in talks_progress):
                print(stage_5Coffee["JeniferRepeat"])
        elif not stage_6Coffee["Completion"]:
            print(stage_6Coffee["JeniferRepeat"])
    elif STORY_DOUBLE_STARTED in story_progress:
        if not stage_4Agent["Completion"]:
            print(stage_4Agent["JeniferRepeat"])
        elif not stage_5Agent["Completion"]:
            print(stage_5Agent["JeniferRepeat"])


def debra_talks(current_room):
    from player import story_progress
    global talks_progress
    if not stage_3["Completion"]:
        if not (STORY_TALKED_DEBRA_S2 in talks_progress):
            talks_progress.append(STORY_TALKED_DEBRA_S2)
            print(stage_2["Debra"])
        elif (STORY_TALKED_DEBRA_S2 in talks_progress):
            print(stage_2["DebraRepeat"])
    elif not stage_3_4["Completion"]:
        print(stage_3["DebraRepeat"])
    elif STORY_COFFEE_STARTED in story_progress:
        if not stage_4_2C["Completion"]:
            if not (STORY_TALKED_DEBRA_S4C in talks_progress):
                talks_progress.append(STORY_TALKED_DEBRA_S4C)
                print(stage_4Coffee["DebraStart"])
            elif (STORY_TALKED_DEBRA_S4C in talks_progress):
                print(stage_4Coffee["DebraRepeat"])
        elif not stage_5Coffee["Completion"]:
            if not (STORY_TALKED_DEBRA_S5C in talks_progress):
                talks_progress.append(STORY_TALKED_DEBRA_S5C)
                print(stage_5Coffee["DebraStart"])
            elif (STORY_TALKED_DEBRA_S5C in talks_progress):
                print(stage_5Coffee["DebraRepeat"])
        elif not stage_6Coffee["Completion"]:
            print(stage_6Coffee["DebraRepeat"])
    elif STORY_DOUBLE_STARTED in story_progress:
        if not stage_4Agent["Completion"]:
            print(stage_4Agent["DebraRepeat"])
        elif not stage_5Agent["Completion"]:
            print(stage_5Agent["DebraRepeat"])


def bob_talks(current_room):
    from player import story_progress
    global talks_progress
    if not stage_3["Completion"]:
        if not (STORY_TALKED_BOB_S2 in talks_progress):
            talks_progress.append(STORY_TALKED_BOB_S2)
            print(stage_2["Bob"])
        elif (STORY_TALKED_BOB_S2 in talks_progress):
            print(stage_2["BobRepeat"])
    elif not stage_3_4["Completion"]:
        if not (STORY_TALKED_BOB_S3 in talks_progress):
            talks_progress.append(STORY_TALKED_BOB_S3)
            print(stage_3["BobStart"])
        elif (STORY_TALKED_BOB_S3 in talks_progress):
            print(stage_3["BobRepeat"])
    elif STORY_COFFEE_STARTED in story_progress:
        if not stage_4_2C["Completion"]:
            if not (STORY_TALKED_BOB_S4C in talks_progress):
                talks_progress.append(STORY_TALKED_BOB_S4C)
                print(stage_4Coffee["BobStart"])
            elif (STORY_TALKED_BOB_S4C in talks_progress):
                print(stage_4Coffee["BobRepeat"])
        elif not stage_5Coffee["Completion"]:
            if not (STORY_TALKED_BOB_S5C in talks_progress):
                talks_progress.append(STORY_TALKED_BOB_S5C)
                print(stage_5Coffee["BobStart"])
            elif (STORY_TALKED_BOB_S5C in talks_progress):
                print(stage_5Coffee["BobRepeat"])
        elif not stage_6Coffee["Completion"]:
            print(stage_6Coffee["BobRepeat"])
    elif STORY_DOUBLE_STARTED in story_progress:
        if not stage_4Agent["Completion"]:
            print(stage_4Agent["BobRepeat"])
        elif not stage_5Agent["Completion"]:
            print(stage_5Agent["BobRepeat"])


def stephen_talks(current_room):
    from player import story_progress
    global talks_progress
    if not stage_3["Completion"]:
        print(stage_3["StephenStart"])
        story_progress.append(STORY_TALKED_TO_STEPHEN)
    elif not stage_3_4["Completion"] and STORY_TALKED_TO_STEPHEN in story_progress:
        print(stage_3["StephenRepeat"])
    elif STORY_COFFEE_STARTED in story_progress:
        if not stage_4_2C["Completion"]:
            print(stage_4Coffee["StephenRepeat"])
        elif not stage_5Coffee["Completion"]:
            if not (STORY_TALKED_STEPHEN_S5C in talks_progress):
                talks_progress.append(STORY_TALKED_STEPHEN_S5C)
                print(stage_5Coffee["StephenStart"])
            elif (STORY_TALKED_STEPHEN_S5C in talks_progress):
                print(stage_5Coffee["StephenRepeat"])
        elif not stage_6Coffee["Completion"]:
            print(stage_6Coffee["StephenRepeat"])
    elif STORY_DOUBLE_STARTED in story_progress:
        if not stage_4Agent["Completion"]:
            print(stage_4Agent["StephenRepeat"])
        elif not stage_5Agent["Completion"]:
            print(stage_5Agent["StephenRepeat"])


def alexa_talks(current_room):
    from player import story_progress
    global talks_progress
    if not stage_3["Completion"]:
        if not (STORY_TALKED_ALEXA_S2 in talks_progress):
            talks_progress.append(STORY_TALKED_ALEXA_S2)
            print(stage_2["Alexa"])
        elif (STORY_TALKED_ALEXA_S2 in talks_progress):
            print(stage_2["AlexaRepeat"])
    elif not stage_3_4["Completion"]:
        if not stage_3_1["Completion"]:
            if not (STORY_TALKED_ALEXA_S3 in talks_progress):
                talks_progress.append(STORY_TALKED_ALEXA_S3)
                print(stage_3["AlexaStart"])
            elif (STORY_TALKED_ALEXA_S3 in talks_progress):
                print(stage_3["AlexaRepeat1"])
        elif stage_3_1["Completion"]:
            if not (STORY_TALKED_ALEXA_S31 in talks_progress):
                talks_progress.append(STORY_TALKED_ALEXA_S31)
                print(stage_3["AlexaFound"])
            elif (STORY_TALKED_ALEXA_S31 in talks_progress):
                print(stage_3["AlexaRepeat2"])
    elif STORY_COFFEE_STARTED in story_progress:
        if not stage_4_2C["Completion"]:
            if not (STORY_TALKED_ALEXA_S4C in talks_progress):
                talks_progress.append(STORY_TALKED_ALEXA_S4C)
                print(stage_4Coffee["AlexaStart"])
            elif (STORY_TALKED_ALEXA_S4C in talks_progress):
                print(stage_4Coffee["AlexaRepeat"])
        elif not stage_5Coffee["Completion"]:
            if not (STORY_TALKED_ALEXA_S5C in talks_progress):
                talks_progress.append(STORY_TALKED_ALEXA_S5C)
                print(stage_5Coffee["AlexaStart"])
            elif (STORY_TALKED_ALEXA_S5C in talks_progress):
                print(stage_5Coffee["AlexaRepeat"])
        elif not stage_6Coffee["Completion"]:
            print(stage_6Coffee["AlexaRepeat"])
    elif STORY_DOUBLE_STARTED in story_progress:
        if not stage_4Agent["Completion"]:
            if not (STORY_TALKED_ALEXA_S4A in talks_progress):
                talks_progress.append(STORY_TALKED_ALEXA_S4A)
                print(stage_4Agent["AlexaStart"])
            elif (STORY_TALKED_ALEXA_S4A in talks_progress):
                print(stage_4Agent["AlexaRepeat"])
        elif not stage_5Agent["Completion"]:
            print(stage_5Agent["AlexaRepeat"])