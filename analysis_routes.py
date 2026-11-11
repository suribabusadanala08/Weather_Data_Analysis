from flask import Blueprint, render_template
from backend.security.authentication import login_required
from backend.services.weather_service import get_states

analysis_bp = Blueprint("analysis", __name__)

@analysis_bp.get("/analysis")
@login_required
def analysis():
    return render_template("analysis.html", states=get_states())
