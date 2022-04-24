from django.core.management.base import BaseCommand
from random import randrange
from comment_api.utils import random_date
from datetime import datetime
from apis.models import Comment, Reply


class Command(BaseCommand):
    help = "Assign days to comments and replies already existing"

    def handle(self, *args, **kwargs):
        comments = Comment.objects.all()
        replies = Reply.objects.all()
        years = [
            2001, 2002, 2003, 2004,
            2005, 2006, 2007, 2008,
            2009, 2010, 2011, 2013,
            2019
        ]
        d1 = None
        d2 = None
        arg = None
        for year in years:
            date = f'1/1/{year} 1:30 PM'
            val = randrange(20)
            y_delta = year + val
            date_2 = f'1/1/{y_delta} 4:50 AM'

            d1 = datetime.strptime(date, '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime(date_2, '%m/%d/%Y %I:%M %p')
            arg = datetime.now() - d1
            arg = str(arg).split(" ")

        print(d1, d2)
        print(random_date(d1, d2))
        for comment in comments:
            comment.date = f"{randrange(int(arg[0]))} days ago"
            comment.save(update_fields=["date"])

        print(f"All done, {comments.count()} Total")

        for reply in replies:
            reply.date = f"{randrange(int(arg[0]))} days ago"
            reply.save(update_fields=["date"])

        print(f"All done, {replies.count()} Total")
