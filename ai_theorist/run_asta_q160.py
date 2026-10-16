"""Asta MCP searches q160-q173 for the AI-theorist section (9 October 2026)."""
import json, subprocess, sys, pathlib
Q = [
 ("q160_llm_hypothesis_generation_materials", "large language model hypothesis generation materials science"),
 ("q161_ai_scientist_automated_discovery", "AI scientist automated open-ended scientific discovery language model agents"),
 ("q162_sr_background_theory_derivable", "symbolic regression background theory logical reasoning derivable"),
 ("q163_llm_guided_symbolic_regression", "LLM guided symbolic regression equation discovery scientific priors"),
 ("q164_ai_coscientist", "AI co-scientist multi-agent hypothesis generation biomedical"),
 ("q165_literature_theory_generation", "literature-grounded theory generation language models scientific theories"),
 ("q166_hypothesis_falsification_agent", "automated hypothesis validation sequential falsification agents"),
 ("q167_llm_hypothesis_autonomous_lab", "hypothesis-driven autonomous laboratory language model agent closed loop"),
 ("q168_llm_novel_ideas_eval", "can language models generate novel research ideas human study"),
 ("q169_kg_hypothesis_materials", "knowledge graph hypothesis generation materials discovery language model"),
 ("q170_ai_physicist_theories", "AI physicist learning theories unsupervised divide and conquer"),
 ("q171_llm_thermal_conductivity_mechanism", "language model phonon thermal conductivity mechanism hypothesis"),
 ("q172_hypothesis_hacking_llm", "LLM generated hypotheses p-hacking post hoc multiple testing reproducibility"),
 ("q173_theory_revision_machine", "machine scientific theory revision anomaly abduction"),
]
cli = sys.argv[1]
out = pathlib.Path(sys.argv[2])
for name, kw in Q:
    p = out / f"{name}_asta.json"
    if p.exists():
        continue
    r = subprocess.run([sys.executable, cli, "search_papers_by_relevance",
                        json.dumps({"keyword": kw, "limit": 20,
                                    "fields": "title,year,venue,externalIds,citationCount,abstract"})],
                       capture_output=True, text=True, timeout=300)
    p.write_text(r.stdout if r.returncode == 0 else json.dumps({"error": r.stderr[-800:]}))
    print(name, r.returncode, len(r.stdout))
