CSS = """
<style>
:root{
  --bg:#080d18;--panel:rgba(18,27,44,.78);--line:rgba(164,183,219,.16);
  --text:#edf4ff;--muted:#9aa8c1;--gold:#d8b86c;--gold2:#b9954c;--cyan:#63d7ff;
}
html,body,[data-testid="stAppViewContainer"]{
  background:
    radial-gradient(circle at 8% 0%,rgba(74,113,255,.13),transparent 30%),
    radial-gradient(circle at 92% 0%,rgba(216,184,108,.08),transparent 24%),
    linear-gradient(180deg,#070c17 0%,#0b1020 48%,#070a12 100%);
  color:var(--text);
}
[data-testid="stHeader"]{background:rgba(8,13,24,0)}
[data-testid="stToolbar"]{display:none}
.block-container{padding-top:1.35rem;padding-bottom:4rem;max-width:1480px}

.hero-clean{
  position:relative;display:flex;align-items:center;justify-content:center;
  min-height:104px;border:1px solid rgba(216,184,108,.22);
  background:linear-gradient(135deg,rgba(14,23,39,.92),rgba(9,15,28,.74));
  border-radius:24px;padding:22px 34px;box-shadow:0 22px 60px rgba(0,0,0,.30);
  overflow:hidden;
}
.hero-clean:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(216,184,108,.10),transparent 28%,transparent 72%,rgba(99,215,255,.08));pointer-events:none}
.hero-clean:after{content:"";position:absolute;right:-120px;top:-160px;width:360px;height:360px;background:radial-gradient(circle,rgba(99,215,255,.13),transparent 64%);pointer-events:none}
.hero-title{position:relative;z-index:1;font-size:2.55rem;line-height:1;font-weight:880;letter-spacing:-.055em;color:#fff;text-align:center;text-shadow:0 14px 34px rgba(0,0,0,.45)}
.buildwell-emblem{position:absolute;right:24px;bottom:18px;width:188px;max-width:20vw;height:auto;z-index:2;filter:drop-shadow(0 14px 26px rgba(0,0,0,.45));border:0!important;background:transparent!important}

.metric-card{border:1px solid var(--line);background:linear-gradient(180deg,rgba(20,31,51,.82),rgba(12,19,33,.72));border-radius:22px;padding:20px;min-height:112px;box-shadow:0 16px 44px rgba(0,0,0,.23)}
.metric-label{color:var(--muted);text-transform:uppercase;letter-spacing:.12em;font-size:.72rem;font-weight:800}.metric-value{color:#fff;font-size:2.2rem;font-weight:800;letter-spacing:-.04em;margin-top:8px}.metric-note{color:#aab6cc;font-size:.87rem;margin-top:7px;line-height:1.35}
.section-title{margin-top:34px;margin-bottom:16px;font-size:1.28rem;font-weight:850;letter-spacing:-.025em;color:#fff}.section-subtitle{display:none}
.lane-card{border:1px solid var(--line);background:rgba(14,22,36,.62);border-radius:18px;padding:16px;min-height:92px}.lane-title{color:#fff;font-weight:850;font-size:1rem}.lane-metrics{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.lane-metrics span{border:1px solid rgba(216,184,108,.18);background:rgba(216,184,108,.055);color:#f2deaa;border-radius:999px;padding:5px 9px;font-size:.76rem}
.signal{border-left:3px solid rgba(99,215,255,.85);background:rgba(99,215,255,.055);border-radius:14px;padding:12px 14px;margin-bottom:10px;color:#dceaff}.signal strong{color:#fff}.caption{display:none}

/* Button: centered, premium, not default Streamlit green. */
div[data-testid="stButton"]{display:flex;justify-content:center;margin:10px 0 12px 0}
div[data-testid="stButton"] button{
  width:100%;max-width:300px;border-radius:999px;min-height:50px;
  border:1px solid rgba(216,184,108,.48)!important;
  background:linear-gradient(135deg,rgba(216,184,108,.96),rgba(177,143,72,.92))!important;
  color:#08101e!important;font-weight:900!important;letter-spacing:.01em;
  box-shadow:0 14px 34px rgba(0,0,0,.30), inset 0 1px 0 rgba(255,255,255,.28)!important;
}
div[data-testid="stButton"] button:hover{border-color:rgba(255,226,158,.78)!important;transform:translateY(-1px)}
.stPlotlyChart{border-radius:22px;overflow:hidden;border:1px solid rgba(164,183,219,.10);background:rgba(7,12,22,.18)}

/* Dark select/dropdown cleanup */
div[data-baseweb="select"]>div, div[data-baseweb="select"] div, div[data-baseweb="input"]>div, input, textarea{
  background-color:rgba(12,19,33,.96)!important;border-color:rgba(164,183,219,.22)!important;color:#edf4ff!important;
}
div[data-baseweb="select"]>div{border-radius:14px!important}
div[data-baseweb="select"] span, div[data-baseweb="select"] svg, div[data-baseweb="input"] input{color:#edf4ff!important;fill:#edf4ff!important}
div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"], div[role="listbox"]{
  background:#0d1526!important;color:#edf4ff!important;border:1px solid rgba(164,183,219,.22)!important;
}
li[role="option"], div[role="option"]{background:#0d1526!important;color:#edf4ff!important}
li[role="option"]:hover, div[role="option"]:hover{background:rgba(99,215,255,.10)!important}
[data-testid="stSelectbox"], [data-testid="stMultiSelect"]{color:#edf4ff!important}

/* Expander cleanup: remove the white header bars Streamlit can inject. */
div[data-testid="stExpander"]{border:1px solid rgba(164,183,219,.16)!important;border-radius:16px!important;background:rgba(10,16,28,.42)!important;overflow:hidden!important;box-shadow:none!important}
div[data-testid="stExpander"] details{background:rgba(10,16,28,.42)!important;color:#edf4ff!important}
div[data-testid="stExpander"] summary, div[data-testid="stExpander"] summary:hover{
  background:linear-gradient(90deg,rgba(17,27,46,.96),rgba(12,19,33,.92))!important;color:#edf4ff!important;border-bottom:1px solid rgba(164,183,219,.12)!important;
}
div[data-testid="stExpander"] summary *{color:#edf4ff!important;fill:#edf4ff!important}
div[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p{color:#edf4ff!important}

/* Native dataframe fallback styling */
div[data-testid="stDataFrame"], div[data-testid="stDataFrame"] div{background:rgba(10,16,28,.78)!important;color:#edf4ff!important;border-color:rgba(164,183,219,.16)!important}
div[data-testid="stDataFrame"] *{color:#edf4ff!important}
.dark-table-wrap{overflow:auto;border:1px solid var(--line);border-radius:18px;background:rgba(10,16,28,.78);box-shadow:0 16px 42px rgba(0,0,0,.18);margin-bottom:14px}.dark-data-table{border-collapse:separate;border-spacing:0;width:100%;font-size:.82rem;color:#edf4ff}.dark-data-table thead th{position:sticky;top:0;background:#111b2e;color:#fff;text-align:left;padding:10px 12px;border-bottom:1px solid rgba(164,183,219,.22);white-space:nowrap;z-index:2}.dark-data-table tbody td{padding:9px 12px;border-bottom:1px solid rgba(164,183,219,.10);color:#dce7f7;vertical-align:top;max-width:360px}.dark-data-table tbody tr:nth-child(even){background:rgba(255,255,255,.025)}.dark-data-table tbody tr:hover{background:rgba(99,215,255,.06)}

@media(max-width:900px){.hero-title{font-size:2rem}.buildwell-emblem{position:relative;right:auto;bottom:auto;width:150px;max-width:52vw;margin-left:16px}.hero-clean{justify-content:space-between;padding:20px 22px}}
</style>
"""
