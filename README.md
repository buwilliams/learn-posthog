# Learn PostHog

This repo is where I'm working on sample projects to help me learn the tech stack at PostHog. I'm an experienced developer and new to most of PostHog's tech stack and source code.

## Notes about learning

Some people like to jump in. Some people like to read the docs. I'm the later. My plan is to spend part of the time accomplishing work given to me and part of the time reading to supplement knowledge gaps. The point is to know your own learning style so that you can be effective.

It's also important to note that whatever you learn needs to be reviewed several times. It doesn't matter what learning style you have because review is essential to learning from a nueroscientific perspective. If you create small exercises for yourself such as the projects I've created in this repo you'll do even better. The good news is that this process doesn't take up a extraordinary amount of time.

## A word about mindset

> You get more than what you give.

My mindset is one of wanting to get the most out of life. For me, in part, that means being excellent and taking full ownership of my career. Learning new material can be overwhelming not to mention difficult. But remember this: *it's worth it*! Investing in yourself makes for a better, more capable version of you. Therefore, trust the difficult process of learning and elevate your skills. The future you will thank you for your hard work.

## Tech to learn (in no particular order)

- [x] [React](https://reactjs.org/docs/hello-world.html)
- [x] [Redux](https://redux.js.org/introduction/core-concepts)
- [x] [Kea](https://kea.js.org/docs/introduction/what-is-kea)
- [ ] [TypeScript](https://www.typescriptlang.org/)
- [ ] [Python](https://www.python.org/)
- [ ] [Django](https://www.djangoproject.com/)
- [ ] [Django Testing](https://docs.djangoproject.com/en/3.1/intro/tutorial05/)
- [ ] [Pytest](https://docs.pytest.org/en/stable/getting-started.html)
- [ ] [Clickhouse](https://clickhouse.tech/)

## Suggested learning roadmap

1. [Setup your local dev environment](https://posthog.com/docs/developing-locally) and [Apple Silicon](https://github.com/PostHog/posthog/issues/2916)
2. Ask your [PostHog Buddy](https://posthog.com/handbook/people/onboarding#posthog-buddy) for a product walk-thru. It's important to get to know the product you are building. I recommend doing this before you become deeply involved in it's internal design. This is a great time to view our product through the eyes of our uesrs.
3. [Review PostHog Project Structure](https://posthog.com/docs/project-structure)
4. Learn [React](https://reactjs.org/docs/hello-world.html), [Redux](https://redux.js.org/introduction/core-concepts), and [Kea](https://kea.js.org/docs/introduction/what-is-kea) - If you're experienced with frontend frameworks I suggest going directly to Kea.
5. Take a brief overview of [Python](https://learnxinyminutes.com/docs/python/).
6. Complete [Django Tutorial 1-5 of 7 parts, skip 6+](https://docs.djangoproject.com/en/3.1/intro/tutorial01/). If you're interested in learning more about Django, pick a copy of [Django book](https://www.feldroy.com/products/two-scoops-of-django-3-x). The company will happily pay for this since they [believe in training us to do our jobs with excellent](https://posthog.com/handbook/people/training). Great place to work, right?

## Great places to learn

### Python

- [Python via LearnXinYminutes](https://learnxinyminutes.com/docs/python/)
- [Writing your first Django app](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) - I recommend reading Parts 1-5 of the 7 parts, skip 6+ since they are not relevent to PostHog. We do use Django built-in testing so part 5 is required reading.
- [Two Scoops of Django (e-book)](https://www.feldroy.com/products/two-scoops-of-django-3-x)

## What has helped me technically

- [Setup local dev on M1 chip aka. Apple Silicon](https://github.com/PostHog/posthog/issues/2916)
- [Navigating PostHog Source Code](https://posthog.com/docs/project-structure)
- [Switch between Postgres and Clickhouse](https://github.com/PostHog/posthog/blob/master/posthog/api/__init__.py) - PostHog uses two databases. Often the same backend work will be duplicated for these two databases since the queries will be different. The link shows you where the swap takes place. This is an important feature to know about early on. My first PR was broken for Clickhouse but worked fine for Postgres.

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
- Additionally, it's important to remember to trust the process. Being new (bad) at something isn't a great feeeling initially until you realize that it's a part of the process. Soon you'll be good. It's better to reframe and remember that you only get to have new eyes once. Plus, it's fun to learn new things.

> "When you are working, close your email and slack. No one is watching to see if you are online. In fact, it's the opposite." - Tim, CTO

- Tim told me this on the first or second day and it was liberating. It allowed me to think of my role as a true `async` open-source contributor. Do what needs to be done so that you can be the most effective.

> Read the docs

- For my learning style, this has been a **must**. I'm keeping a list of resources for learning I've used.
- I also spent time creating projects as you see in this repo. These helps me reenforce and consolidate the knowledge I was gaining.

## This Repo's Docs

- [Kea](docs/kea.md)
- [Python](docs/python.md)
- [Django](docs/django.md)
