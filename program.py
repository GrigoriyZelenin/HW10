from flask import Flask
from utils import get_all_candidates, format_candidates, get_candidate_by_id, get_candidate_by_skill

app = Flask(__name__)

# if __name__ == "__main__":

@app.route("/")
def maine_page():
    candidates: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result


@app.route("/candidates/<int:uid>")
def candidate_page(uid):
    candidate: dict = get_candidate_by_id(uid)
    result = f"<img src='{candidate['picture']}'>"
    result += format_candidates([candidate])
    return result

@app.route("/skills/<skill>")
def skill_page(skill):
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result

app.run()