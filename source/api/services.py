from .models import Action

def action_create(user, text, task=None, project=None):
    if task:
        action = Action.objects.create(
            user=user,
            text=text,
            task=task
        )
        print(action.project, action.text, action.task)
    elif project:
        action = Action.objects.create(
            user=user,
            text=text,
            project=project

        )
        print(action.project, action.text, action.task)
    else:
        action = Action.objects.create(
            user=user,
            text=text
        )
        print(action.user, action.text)

    return True


