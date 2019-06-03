---
title: 'Project documentation template'
disqus: hackmd
---

MyPosts
===

## Table of Contents

[TOC]

## Overview


1. Each user can create edit delete any of his pastes.
2. Anonymous guests can create posts as well. but it's status will be public
3. Each user can filter pastes by dates.
4. Helper scripts to export statistics about the project in csv (eg. Number of pastes for each user)
5. Each paste can be either shared to public or a certain users or set to private only for the creator

How to use?
---
> pip install -r requirements.txt
> python manage.py shell
>
then copy and paste this commands into the shell
```python
from posts.models import *
from django.contrib.auth.models import User
user1=User(username="user_1")
user1.set_password("25632541")
user1.save()
user2=User(username="user_2")
user2.set_password("25632541")
user2.save()

post1 = Post(post_details="user1 private post",owner=user1,status="PRIVATE")
post1.save()
post2 = Post(post_details="user1 public post",owner=user1,status="PUBLIC")
post2.save()

post1 = Post(post_details="user2 private post",owner=user2,status="PRIVATE")
post1.save()
post2 = Post(post_details="user2 public post",owner=user2,status="PUBLIC")
post2.save()

```
### running the servver and Test the app
> python manage.py runserver 

from another terminal you can use curl or HTTPie
>get all posts by annoynous user 

![image](https://drive.google.com/uc?export=view&id=1iM4JTThj7QSebaGSvFtau8TKvFdnWK87)

>get all posts by user2 user 
>notice now we can get the private post created by user2

![image](https://drive.google.com/uc?export=view&id=1uGbafhYa9zoTOboHxxgwMpRTL50xIc75)


>get all posts by user1 user 
>notice now we can get the private post created by user2 also because user2 share his private post with user1

![image](https://drive.google.com/uc?export=view&id=1QDhjVpk8z_snPeWzrU-HSUCexbC5YKYI)
>in the blow images i tried to delete post created by user1 the first attempt was deleting post by anonymous user in the sceond successful attempt i tried delting image using cardinals of it's owner


![image](https://drive.google.com/uc?export=view&id=1c3ECLvzLPJ6YHWAsu5GCW_bWVjFXoOXK)

![image](https://drive.google.com/uc?export=view&id=1_DXkRrLPzK01RoDFP7Yg2tk_GGY2HAs1)

>Here we try to Update the detials in the post 

![image](https://drive.google.com/uc?export=view&id=1bdacdpQEbflzn9JvZhqetu79Fad90x2o)


>Here we try to Post  new  post  by anonymous and registered one 

![image](https://drive.google.com/uc?export=view&id=1wERxbHwYwH5T5g_rSzrRKfakqGC16EsP)

>to Donload filter posts by date 

![image](https://drive.google.com/uc?export=view&id=1bDTL1_duxMMG2xkmsDP-hYPO5pw040pS)


![image](https://drive.google.com/uc?export=view&id=1aDZpNi6J0wmRH09qMoFLX2b985GdJXhw)

>to Download Statistics File about the users

![image](https://drive.google.com/uc?export=view&id=1fcwIjhQTBaTTLMszvGzt3sX2guzyuQVp)

![image](https://drive.google.com/uc?export=view&id=1Eu4h8Muj8Qo8BYVIt2k1yj5pFZ69Y-1m)


## ToDo
1. Token-based authentication system.
2. Basic UI 
3. give Each post shortened URL
4. Use more Filters 
