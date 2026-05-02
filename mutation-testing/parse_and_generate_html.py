import re
from datetime import datetime

# Read the mutant results file
with open('mutant_results.txt', 'r') as f:
    content = f.read()

# Parse survivors from features.py
features_survived = []
scoring_survived = []
scoring_no_tests = []

for line in content.split('\n'):
    if 'survived' in line:
        if 'pipeline.features' in line:
            mutant_id = line.strip().split(':')[0].strip()
            features_survived.append(mutant_id)
        elif 'pipeline.scoring' in line and 'get_driver_tier' in line:
            mutant_id = line.strip().split(':')[0].strip()
            scoring_survived.append(mutant_id)
    elif 'no tests' in line and 'pipeline.scoring' in line:
        if 'RidgeRanker' in line or 'rank_drivers' in line:
            mutant_id = line.strip().split(':')[0].strip()
            scoring_no_tests.append(mutant_id)

# Counts
total_features_survived = len(features_survived)
total_scoring_survived = len(scoring_survived)
total_scoring_no_tests = len(scoring_no_tests)
total_survived = total_features_survived + total_scoring_survived
total_mutants = 441
killed = 209
survived = 173
runtime_errors = 59
mutation_score = round(killed / total_mutants * 100, 1)

# Generate HTML
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mutation Testing Report - AutoAid</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
            color: white;
            padding: 30px 40px;
        }}
        .header h1 {{ font-size: 32px; margin-bottom: 10px; }}
        .header p {{ opacity: 0.9; font-size: 14px; }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px 40px;
            background: #f8f9fa;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            transition: transform 0.3s;
        }}
        .stat-card:hover {{ transform: translateY(-5px); }}
        .stat-card .number {{
            font-size: 48px;
            font-weight: bold;
            margin: 10px 0;
        }}
        .stat-card .label {{ color: #666; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }}
        .killed .number {{ color: #27ae60; }}
        .survived .number {{ color: #e74c3c; }}
        .score .number {{ color: #3498db; }}
        .content {{ padding: 30px 40px; }}
        .section {{
            margin-bottom: 30px;
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
        }}
        .section h2 {{
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #3498db;
            display: inline-block;
        }}
        .mutant-list {{
            list-style: none;
            max-height: 300px;
            overflow-y: auto;
        }}
        .mutant-list li {{
            padding: 8px 12px;
            margin: 5px 0;
            background: white;
            border-radius: 8px;
            font-family: monospace;
            font-size: 12px;
            border-left: 4px solid #e74c3c;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }}
        .badge-survived {{ background: #fee; color: #e74c3c; }}
        .badge-no-tests {{ background: #e3f2fd; color: #2196f3; }}
        .footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 12px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background: #2c3e50;
            color: white;
        }}
        tr:hover {{ background: #f5f5f5; }}
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>🧬 Mutation Testing Report</h1>
        <p><strong>Project:</strong> AutoAid Recommender API</p>
        <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p><strong>Target Module:</strong> pipeline/features.py + pipeline/scoring.py</p>
    </div>

    <div class="stats">
        <div class="stat-card">
            <div class="label">Total Mutants</div>
            <div class="number">{total_mutants}</div>
        </div>
        <div class="stat-card killed">
            <div class="label">✅ Killed</div>
            <div class="number">{killed}</div>
        </div>
        <div class="stat-card survived">
            <div class="label">❌ Survived</div>
            <div class="number">{survived}</div>
        </div>
        <div class="stat-card">
            <div class="label">⏰ Runtime Errors</div>
            <div class="number">{runtime_errors}</div>
        </div>
        <div class="stat-card score">
            <div class="label">🎯 Mutation Score</div>
            <div class="number">{mutation_score}%</div>
        </div>
    </div>

    <div class="content">
        <div class="section">
            <h2>📊 Results Summary</h2>
            <table>
                <tr><th>Metric</th><th>Value</th></tr>
                <tr><td>Mutants Killed</td><td>{killed}</td></tr>
                <tr><td>Mutants Survived</td><td>{survived}</td></tr>
                <tr><td>Mutants Timed Out</td><td>0</td></tr>
                <tr><td>Equivalent Mutants (est.)</td><td>0</td></tr>
                <tr><td>Mutation Score</td><td>{mutation_score}%</td></tr>
                <tr><td>Baseline Line Coverage</td><td>62%</td></tr>
                <tr><td>Coverage-Score Gap</td><td>{62 - mutation_score} pp</td></tr>
            </table>
        </div>

        <div class="section">
            <h2>❌ Survived Mutants in features.py</h2>
            <p><strong>Total:</strong> {total_features_survived} mutants survived</p>
            <ul class="mutant-list">
                {''.join([f'<li>{m}</li>' for m in features_survived[:30]])}
                {f'<li>... and {total_features_survived - 30} more</li>' if total_features_survived > 30 else ''}
            </ul>
        </div>

        <div class="section">
            <h2>❌ Survived Mutants in scoring.py (get_driver_tier)</h2>
            <p><strong>Total:</strong> {total_scoring_survived} mutants survived</p>
            <ul class="mutant-list">
                {''.join([f'<li>{m}</li>' for m in scoring_survived])}
            </ul>
        </div>

        <div class="section">
            <h2>📋 Task 3 Analysis Mutants (Selected)</h2>
            <table>
                <tr><th>#</th><th>Mutant ID</th><th>Function</th><th>Operator</th></tr>
                <tr><td>M1</td><td><code>x_get_driver_tier__mutmut_17</code></td><td>get_driver_tier()</td><td><span class="badge badge-survived">LCR</span></td></tr>
                <tr><td>M2</td><td><code>x_bayesian_rating__mutmut_1</code></td><td>bayesian_rating()</td><td><span class="badge badge-survived">AOR</span></td></tr>
                <tr><td>M3</td><td><code>x_distance_score__mutmut_1</code></td><td>distance_score()</td><td><span class="badge badge-survived">ROR</span></td></tr>
                <tr><td>M4</td><td><code>x_cancel_score__mutmut_2</code></td><td>cancel_score()</td><td><span class="badge badge-survived">BCR</span></td></tr>
            </table>
        </div>

        <div class="section">
            <h2>📝 Commands to Inspect Mutants</h2>
            <ul class="mutant-list">
                <li><code>mutmut show pipeline.scoring.x_get_driver_tier__mutmut_17</code> - View LCR mutant</li>
                <li><code>mutmut show pipeline.features.x_bayesian_rating__mutmut_1</code> - View AOR mutant</li>
                <li><code>mutmut show pipeline.features.x_distance_score__mutmut_1</code> - View ROR mutant</li>
                <li><code>mutmut show pipeline.features.x_cancel_score__mutmut_2</code> - View BCR mutant</li>
            </ul>
        </div>
    </div>

    <div class="footer">
        <p>Generated by mutmut | AutoAid Mutation Testing Assignment | FAST NUCEs Spring 2025</p>
    </div>
</div>
</body>
</html>'''

with open('reports/mutation_baseline/index.html', 'w') as f:
    f.write(html)

print("✅ HTML Report generated at reports/mutation_baseline/index.html")
print(f"   Total Features Survived: {total_features_survived}")
print(f"   Total Scoring Survived: {total_scoring_survived}")
print(f"   Total Survived: {total_survived}")
