# Sprint Plan

## User stories
1. **Freshman:** As an incoming freshman, I want to ask what documents I need to enroll so I can prepare before going to school.
   - Criteria: Asking "What documents do I need?" returns the requirements answer and FAQ ids 1 and 3.
   - Criteria: The reply is in the language I wrote in (English, Filipino, or Taglish).
2. **Parent:** As a parent, I want to know if tuition can be paid in installments so I can budget.
   - Criteria: The answer lists the four installment points and cites FAQ id 7.
   - Criteria: Questions the FAQ does not cover get "I don't know" plus the Registrar contact, not a guess.
3. **Registrar staff:** As registrar staff, I want to see which question types come up most so I can plan staffing.
   - Criteria: /admin shows questions per category from the classifier.
   - Criteria: /admin shows the percentage of thumbs-up replies.

## Backlog
| Task | Status |
|---|---|
| Write PLAN.md | Done |
| Write faq.json (17 entries, 5 categories) | Done |
| POST /api/chat with validation and top-3 retrieval | Done |
| Gemini grounded prompt | Done |
| intents.csv, train.py, load model in Flask | Done |
| Mobile chat page, ratings, /api/stats, /admin | Done |
| EVAL.md (10 tests, run on deployed app) | To Do |
| Deploy to Render, test on phone | To Do |
| REFLECTION.md answers | To Do |
| Screen recording | To Do |
