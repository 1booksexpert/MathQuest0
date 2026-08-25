import os
import glob
import re

root = r'e:\Docs\MathQuest\MQGithub\MathQuest0'
html_files = glob.glob(os.path.join(root, '*.html'))

for filepath in html_files:
    if os.path.basename(filepath) == 'index.html':
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update basic 'home' links
    content = re.sub(
        r'href="#"([^>]*>\s*<span[^>]*>home</span>)',
        r'href="index.html"\1',
        content,
        flags=re.IGNORECASE
    )
    
    # 2. Update dashboard links
    content = re.sub(
        r'href="#"([^>]*>\s*<span[^>]*>dashboard</span>)',
        r'href="mathquest_dashboard.html"\1',
        content,
        flags=re.IGNORECASE
    )
    
    # 3. Update play/solve links
    content = re.sub(
        r'href="#"([^>]*>\s*<span[^>]*>extension</span>)',
        r'href="mathquest_gameplay_calculator.html"\1',
        content,
        flags=re.IGNORECASE
    )
    
    # 4. Update leaderboard links
    content = re.sub(
        r'href="#"([^>]*>\s*<span[^>]*>military_tech</span>)',
        r'href="global_rankings.html"\1',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'href="#"([^>]*>\s*<span[^>]*>emoji_events</span>)',
        r'href="global_rankings.html"\1',
        content,
        flags=re.IGNORECASE
    )
    
    # 5. Update account/profile links
    content = re.sub(
        r'href="#"([^>]*>\s*<span[^>]*>account_circle</span>)',
        r'href="user_profile_sign_up.html"\1',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'href="#"([^>]*>\s*<span[^>]*>person</span>)',
        r'href="user_profile_sign_up.html"\1',
        content,
        flags=re.IGNORECASE
    )
    
    # 6. Global replace for simple text Back/Retroceso
    # Replacing <a ...> Back </a>
    content = re.sub(
        r'href="#"([^>]*>)\s*Back\s*</a>',
        r'href="javascript:history.back()"\1 Back </a>',
        content,
        flags=re.IGNORECASE
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Navigation linked successfully.')
