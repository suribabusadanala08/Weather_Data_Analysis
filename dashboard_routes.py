from flask import Blueprint, render_template, session
from flask_wtf.csrf import generate_csrf

from backend.security.authentication import login_required
from backend.services.weather_service import get_states, state_summary


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.get("/dashboard")
@login_required
def dashboard():

    # Get Indian states and union territories
    states = get_states()

    # Calculate overall weather summary
    summary = state_summary("All India")

    # Generate CSRF token for the logout form
    csrf_token = generate_csrf()

    # Render dashboard
    return render_template(
        "dashboard.html",
        states=states,
        summary=summary,
        user_name=session.get("user_name", "User"),
        csrf_token=csrf_token
    )