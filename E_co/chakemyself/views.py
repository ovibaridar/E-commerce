from django.shortcuts import render
from language_tool_python import LanguageTool

def index(request):
    if request.method == 'POST':
        sentence = request.POST.get('sentence', '')
        language = request.POST.get('language', 'en-US')  # Get selected language or default to English
        tool = LanguageTool(language)
        matches = tool.check(sentence)
        categorized_errors = {}
        for match in matches:
            if match.ruleIssueType not in categorized_errors:
                categorized_errors[match.ruleIssueType] = []
            categorized_errors[match.ruleIssueType].append({
                'message': match.message,
                'suggestions': match.replacements
            })

        return render(request, 'chakemyself/chak.html', {
            'sentence': sentence,
            'language': language,
            'categorized_errors': categorized_errors
        })

    return render(request, 'chakemyself/chak.html')
