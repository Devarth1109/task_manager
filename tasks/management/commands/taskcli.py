from django.core.management.base import BaseCommand, CommandError
from tasks.models import Task

class Command(BaseCommand):
    help = "Task Management CLI"
    
    def add_arguments(self, parser):
        parser.add_argument('action', choices=['list', 'add', 'complete', 'delete'])
        parser.add_argument('--id', type=int)
        parser.add_argument('--title')
        parser.add_argument('--priority', default='medium')
        
    def handle(self, *args, **options):
        action = options['action']
        
        try:
            if action == 'list':
                tasks = Task.objects.all()
                if not tasks.exists():
                    self.stdout.write("No tasks found.")
                    return
                
                for task in tasks:
                    self.stdout.write(
                        f"{task.id}. {task.title} | "
                        f"{task.status} | {task.priority}"
                    )
                    
            elif action == 'add':
                if not options['title']:
                    raise CommandError("Title is required to add a task.")
                
                task = Task.objects.create(
                    title=options['title'],
                    priority=options['priority']
                )
                self.stdout.write(f"Task created: {task.id}")
                
            elif action == 'complete':
                if not options['id']:
                    raise CommandError("Task ID is required")
                
                task = Task.objects.get(id=options['id'])
                task.status = 'completed'
                task.save()
                self.stdout.write("Task marked as completed")
                
            elif action == 'delete':
                if not options['id']:
                    raise CommandError("Task ID is required")
                
                Task.objects.get(id=options['id']).delete()
                self.stdout.write("Task deleted")
                
        except Task.DoesNotExist:
            raise CommandError("Task not found")
        
        except Exception as e:
            raise CommandError(f"Error: {str(e)}")