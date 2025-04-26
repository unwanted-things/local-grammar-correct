import click
from grammar_correct.rules.grammar_rules import GrammarRules
from grammar_correct.spell_check import SpellChecker
from grammar_correct.text_analyzer import TextAnalyzer
from colorama import init, Fore, Style

init()

def print_header(text: str):
    click.echo(f"\n{Fore.BLUE}✨ {text} ✨{Style.RESET_ALL}\n")

def print_section(text: str):
    click.echo(f"\n{Fore.CYAN}📝 {text}{Style.RESET_ALL}")

def print_issue(issue: str):
    click.echo(f"{Fore.RED}⚠️  {issue}{Style.RESET_ALL}")

def print_success(text: str):
    click.echo(f"{Fore.GREEN}✓ {text}{Style.RESET_ALL}")

@click.group()
def cli():
    """Local Grammar Correct - A local grammar correction tool."""
    pass

@cli.command()
@click.argument('text', required=False)
def correct(text):
    """Correct grammar and spelling in the given text."""
    if not text:
        text = click.prompt('Enter text to correct')
    
    print_header("Grammar Correction")
    
    # Original text
    click.echo(f"{Fore.YELLOW}Original text:{Style.RESET_ALL}")
    click.echo(text)
    
    # Initialize tools
    grammar_rules = GrammarRules()
    spell_checker = SpellChecker()
    
    # Get corrections
    corrected_text = spell_checker.correct(text)
    grammar_issues = grammar_rules.check_all_rules(text)
    
    # Display corrected text
    click.echo(f"\n{Fore.GREEN}Corrected text:{Style.RESET_ALL}")
    click.echo(corrected_text)
    
    # Display spelling corrections
    if spell_checker.corrections:
        print_section("Spelling Corrections")
        for original, corrected in spell_checker.corrections.items():
            click.echo(f"{Fore.RED}✗ {original}{Style.RESET_ALL} → {Fore.GREEN}{corrected}{Style.RESET_ALL}")
    
    # Display grammar issues
    if any(issues for issues in grammar_issues.values()):
        print_section("Grammar Issues")
        for category, issues in grammar_issues.items():
            if issues:
                click.echo(f"\n{Fore.MAGENTA}{category.title()}:{Style.RESET_ALL}")
                for issue in issues:
                    print_issue(issue)

@cli.command()
@click.argument('text', required=False)
def analyze(text):
    """Analyze text for various metrics."""
    if not text:
        text = click.prompt('Enter text to analyze')
    
    print_header("Text Analysis")
    
    # Initialize analyzer
    analyzer = TextAnalyzer()
    stats = analyzer.analyze(text)
    
    # Display statistics
    print_section("Basic Statistics")
    click.echo(f"{Fore.CYAN}Word Count:{Style.RESET_ALL} {stats['word_count']}")
    click.echo(f"{Fore.CYAN}Sentence Count:{Style.RESET_ALL} {stats['sentence_count']}")
    click.echo(f"{Fore.CYAN}Average Word Length:{Style.RESET_ALL} {stats['avg_word_length']:.1f}")
    click.echo(f"{Fore.CYAN}Unique Words:{Style.RESET_ALL} {stats['unique_words']}")
    
    # Display insights
    print_section("Text Insights")
    if stats['avg_word_length'] > 5:
        print_success("Text uses sophisticated vocabulary")
    else:
        print_success("Text uses simple vocabulary")
    
    if stats['unique_words'] / stats['word_count'] > 0.7:
        print_success("Text has good vocabulary variety")
    else:
        print_success("Text has some word repetition")

if __name__ == '__main__':
    cli() 