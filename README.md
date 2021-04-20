# Learn PostHog

A project to help me and others get up to speed on PostHog's tech stack and various bits of advice that make working on PostHog even better.

## Notes about learning

Some people like to jump in. Some people like to read the docs. I'm the later. My plan is to spend part of the time accomplishing work given to me and part of the time reading to supplement knowledge gaps. The point is to know your own learning style so that you can be effective.

It's also important to note that whatever you learn needs to be reviewed several times. It doesn't matter what learning style you have because review is essential to learning from a neuroscience perspective. If you create small exercises for yourself such as the projects I've created in this repo you'll do even better. The good news is that this process doesn't take up a extraordinary amount of time.

## A word about mindset

> You get more than you give.

My mindset is one of wanting to get the most out of life. For me, in part, that means being excellent and taking full ownership of my career. Learning new material can be overwhelming not to mention difficult. But remember this: *it's worth it*! Investing in yourself makes for a better, more capable version of you. Therefore, trust the difficult process of learning and elevate your skills. The future you will thank you for your hard work.

## Tech to learn

### Backend

- [x] [Python](https://www.python.org/)
- [x] [Django](https://www.djangoproject.com/)
- [x] [Django Testing](https://docs.djangoproject.com/en/3.1/intro/tutorial05/)
- [x] [Pytest](https://docs.pytest.org/en/stable/getting-started.html)
- [x] [Clickhouse](https://clickhouse.tech/)
- [x] [Celery](https://docs.celeryproject.org/en/stable/)
- [x] [Docker](https://github.com/buwilliams/learn-docker)

### Frontend

- [x] [React](https://reactjs.org/docs/hello-world.html)
- [x] [Redux](https://redux.js.org/introduction/core-concepts)
- [x] [Kea](https://kea.js.org/docs/introduction/what-is-kea)
- [x] [TypeScript](https://www.typescriptlang.org/)

### Our notes on specific tech

- [TypeScript](docs/typescript.md)
- [Kea](docs/kea.md)
- [React](docs/react.md)
- [Python](docs/python.md)
- [Django](docs/django.md)

### Exercises

Along with reading about any given programming language it's necessary to use that 
knowledge. I've prepared exercises that will help you use the knowledge you are 
learning. You can find [all the exercises here](docs/exercises/exercises.md) along 
with advice for exercises in general.

## Suggested learning roadmap

1. [Setup your local dev environment](https://posthog.com/docs/developing-locally) and [Apple Silicon](https://github.com/PostHog/posthog/issues/2916)
2. Ask your [PostHog Buddy](https://posthog.com/handbook/people/onboarding#posthog-buddy) for a product walk-thru. It's important to get to know the product you are building. I recommend doing this before you become deeply involved in it's internal design. This is a great time to view our product through the eyes of our users.
3. [Review PostHog Project Structure](https://posthog.com/docs/project-structure)
4. Learn [React](https://reactjs.org/docs/hello-world.html), [Redux](https://redux.js.org/introduction/core-concepts), and [Kea](https://kea.js.org/docs/introduction/what-is-kea) - If you're experienced with frontend frameworks I suggest going directly to Kea.
5. Take a brief overview of [Python](https://learnxinyminutes.com/docs/python/).
6. Complete [Django Tutorial 1-5 of 7 parts, skip 6+](https://docs.djangoproject.com/en/3.1/intro/tutorial01/). If you're interested in learning more about Django, pick a copy of [Django book](https://www.feldroy.com/products/two-scoops-of-django-3-x). The company will happily pay for this since they [believe in training us to do our jobs with excellent](https://posthog.com/handbook/people/training). Great place to work, right?

## Developer Workflow

If you haven't already, it's worth your time to read [Contributing to PostHog](https://posthog.com/docs/contributing).

IDE's we use: [vscode](https://code.visualstudio.com/) and [pycharm](https://www.jetbrains.com/pycharm/)

### Backend w/ Vscode

1. Create a git branch
2. Start PostHog with `bin/start`
3. Open app in Chrome and login
4. Open Chrome devtools to network tab
5. Navigate to scene (aka screen or page) and click on the area of interest
6. Find network request in devtools and find request
    - Request maps to ./posthog/api/*.py, i.e. http://localhost:8000/api/insight/funnel/?insight=FUNNELS -> ./posthog/api/insight.py:197
7. Make code changes including tests
    - Use [print()](https://realpython.com/python-print/) as needed for debugging
    - Some developers prefer [Pycharm](https://www.jetbrains.com/pycharm/) for local development
8. Run backend tests
    - `bin/tests posthog` runs only posthog tests excluding ee tests
    - `./bin/tests ee/clickhouse/queries/test/test_trends.py -k test_active_user_math` for specific tests
9. Commit changes to git branch
10. Open PR for review
    - Include Github issue number `#1234` which Github will automatically link for you

### Frontend w/ Vscode

1. Same as backend 1-5
2. Find frontend code, i.e. `frontend/src/scenes/insights/Insight.tsx`
3. Use `console.log` liberally
3. As of writing, there are no unit tests for the frontend although we do have integration tests for the frontend via Cypress
4. Same as backend 9-10

### Alternative: Pycharm

Some developers prefer to use [Pycharm](https://www.jetbrains.com/pycharm/) and for 
good reason. While there are many benefits, below you'll find a few keys benefits.

1. `Debugging and no print() statements` this is probably the biggest win in my opinion. 
   Since we are learning a new codebase there is no shame in having an assistant. Pycharm
   will show you the call stack and variable values. This is huge for understanding what
   is going on.
2. `Code navigation` when you are new to a codebase, moving easily through the code
   can be a real challenge, especially when there are multiple layers of abstraction. 
   Pycharm allows you to Ctrl+Click nearly all methods to jump to their definitions.
   While editors like vscode have a similar feature, you'll find that Pycharm works
   in cases where vscode does not.
3. `Run configurations` make starting celery, django, and webpack services simple. It's 
   mostly just clicking things.
4. `Excellent TypeScript support` with code completion and type checking directly in your 
   editor.
5. `Click instead of type` which means that you spend much more time typing code than 
   running commands. Nearly everything in Pycharm is clickable.
   
Pycharm offers a try it for free 30-day trial. It's recommended that you use it for at least 
that amount of time before you buy. I recommend watching [The Future of Programming](https://www.youtube.com/watch?v=8pTEmbeENF4) 
that will blow your mind and perhaps give you a new perspective on tools like these.

## Great places to learn

### Python

- [Python via LearnXinYminutes](https://learnxinyminutes.com/docs/python/)
- [Writing your first Django app](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) - I recommend reading Parts 1-5 of the 7 parts, skip 6+ since they are not relevant to PostHog. We do use Django built-in testing so part 5 is required reading.
- [Two Scoops of Django (e-book)](https://www.feldroy.com/products/two-scoops-of-django-3-x)

### Learn about the people who make PostHog

- It's surprising how enjoyable and calming learning about team that makes PostHog can be. You'll find [all their bios here](https://posthog.com/handbook/company/team). It's well worth your time!

### PostHog via James Hawkins, CEO

- [Why we built our business in the first place](https://www.youtube.com/watch?v=TIxxIEEvczM)
- [Open Source is Eating SaaS](https://www.youtube.com/watch?v=bh3j_9jVeqg)
- [How we raised a $3M seed round a few weeks after starting our open source project](https://www.youtube.com/watch?v=lJ41-95Ey3w)
- [Open source business models - your choices and how PostHog makes money](https://www.youtube.com/watch?v=L1Ovbzs7vyo)
- [We've never met each other in real life. How we designed PostHog for remote work from day one.](https://www.youtube.com/watch?v=rRwzJiljpSA)
- [Coffee + iPads + Feedback = A day in the of PostHog's graphic designer](https://www.youtube.com/watch?v=xlODCLrZyvM) by Lottie (helpful to see the design side of PostHog)

## What has helped me technically

- [Setup local dev on M1 chip aka. Apple Silicon](https://github.com/PostHog/posthog/issues/2916)
- [Navigating PostHog Source Code](https://posthog.com/docs/project-structure)
- [Switch between Postgres and Clickhouse](https://github.com/PostHog/posthog/blob/master/posthog/api/__init__.py) - PostHog uses two databases. Often the same backend work will be duplicated for these two databases since the queries will be different. The link shows you where the swap takes place. This is an important feature to know about early on. My first PR was broken for Clickhouse but worked fine for Postgres.
- Subscribing to Posthog and Posthog.com on GitHub for all notifications via Email. Create a Gmail filter to archive and label them. This allows you to browse everything that is going on each day. It's a great place to get "news" and stay up-to-date. You can create more advanced filters as well, for example, a filter which adds a label for all the things you are directly involved in.
- As of 4/7/2021 PostHog doesn't run Clickhouse or Docker on Apple Macbooks since it requires too much memory. Internally, we use [Remove SSH](https://code.visualstudio.com/docs/remote/ssh) with an AWS devbox.

## What has helped me personally

First thing to remember: starting a new job is like beginning a book in the middle of a 
series where the characters are well formed and the story is far along. It's fair to say, 
you have no idea what is going on. You can read words and understand but not understand 
why they are being said.

*My goal is to develop a solid mental model for the codebase.*

> “You don’t care about the answer until you have the question.” - Unknown

- On my first day, I was given an assignment to work on. It began the process of showing me what I needed to learn. Struggling to complete the assignment helped me to *have the question* from the quote above.
- Reading the [project structure doc](https://posthog.com/docs/project-structure)
- Browsing the [issues in GitHub](https://github.com/PostHog/posthog/issues) by playing with the various labels. This helped me get a better feel for PostHog's communication style and open-mindedness.
- Pairing with Tim & Eric. They used devtools to examine network traffic, console.log, and I was able to ask specific questions. It was basic stuff and reminded me to use the basic tools I've been using for years. I guess the anxiety of a new job confused my brain a little.
- Reading the kea docs. This is *clutch* to understand the frontend. It's a rather nice library but you won't make progress without understanding Kea.
- Creating a simple app with create-react-app with typescript support `yarn create react-app learn-kea-typescript --template typescript`

> "Take care of yourself. There's no need to burnout in the first month." - Eltje

- Eltje encouraged me to take care of myself, so I did.

> "So, what?!" - [Dare: The New Way to End Anxiety and Stop Panic Attacks](https://www.amazon.com/Dare-Anxiety-Stop-Panic-Attacks/dp/0956596258/) where "D" stands for defuse the anxiety by considering the worst and saying so what.

- Often I felt anxious about my daily contributions. Using the quote above really helps deal with this kind of anxiety. So what if I fail to deliver these assignments timely?! I'm an expert and in time I'll be a great asset to PostHog.
- Additionally, it's important to remember to trust the process. Being new (bad) at something isn't a great feeling initially until you realize that it's a part of the process. Soon you'll be good. It's better to reframe and remember that you only get to have new eyes once. Plus, it's fun to learn new things.

> "When you are working, close your email and slack. No one is watching to see if you are online. In fact, it's the opposite." - Tim, CTO

- Tim told me this on the first or second day and it was liberating. It allowed me to think of my role as a true `async` open-source contributor. Do what needs to be done so that you can be the most effective.

> Read the docs

- For my learning style, this has been a **must**. I'm keeping a list of resources for learning I've used.
- I also spent time creating projects as you see in this repo which helped me consolidate the knowledge I was gaining.
