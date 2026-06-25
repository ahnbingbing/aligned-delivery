# VHS tape — aligned-delivery demo (ENGLISH narration)
# Record:  vhs demo.tape   (install: brew install vhs — https://github.com/charmbracelet/vhs)
# Run from the SKILL REPO ROOT so scripts/ and evals/ resolve:
#   cp this file to /Users/ahnbingbing/Documents/Skills/aligned-delivery/ , cd there, then `vhs demo.tape`
# Note: the scripts print bilingual EN/KO labels by design (the skill is bilingual). If you want
#       fully English-only output, ask for a `--lang en` flag on the scripts.

Output demo.gif
Set Theme "Dracula"
Set FontSize 18
Set Width 1280
Set Height 760
Set Padding 20
Set TypingSpeed 55ms

# pause AFTER typing, BEFORE Enter, so the command is readable; then pause to read the output.
Type "echo 'aligned-delivery — a PM skill that ships REAL analytics (stdlib, no deps)'"
Sleep 2s
Enter
Sleep 1500ms

Type "python3 scripts/sprint_predictability.py evals/sprints.csv"
Sleep 2500ms
Enter
Sleep 4500ms

Type "echo '^ leads with scope predictability (the leading indicator); flags fake productivity'"
Sleep 2500ms
Enter
Sleep 1500ms

Type "python3 scripts/flow_metrics.py scripts/sample_flow.csv"
Sleep 2500ms
Enter
Sleep 5s

Type "echo '^ flow efficiency + DORA: deployment frequency, change-failure rate, MTTR'"
Sleep 2500ms
Enter
Sleep 1500ms

Type "python3 scripts/forecast_montecarlo.py scripts/sample_throughput.csv --backlog 50"
Sleep 2500ms
Enter
Sleep 4500ms

Type "echo '^ 85% confidence: done within N periods — forecast from history, no estimates'"
Sleep 3s
Enter
Sleep 2500ms
