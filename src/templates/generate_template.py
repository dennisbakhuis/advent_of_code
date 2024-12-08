"""Generate a new day's template from a template file."""
import sys


def main(template_path: str, output_path: str, year: str, day: str) -> None:
    """
    Generate a templated Python file by substituting placeholders with given year and day.

    Parameters
    ----------
    template_path : str
        The path to the template Python file containing placeholders.
    output_path : str
        The path where the generated file will be written.
    year : str
        The year string to replace $$YEAR$$ in the template.
    day : str
        The day string to replace $$DAY$$ in the template, unpadded.

    Notes
    -----
    The output filename can contain zero-padded day, but inside the file $$DAY$$ is replaced
    without zero-padding.
    """
    day_unpadded = str(int(day))

    with open(template_path, "r") as f:
        template = f.read()

    updated = (template
               .replace("\"'YEAR'\"", year)
               .replace("\"'DAY'\"", day_unpadded))

    with open(output_path, "w") as f:
        f.write(updated)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: generate_template.py <template_path> <output_path> <year> <day>")
        sys.exit(1)
    _, template_path, output_path, year, day = sys.argv
    main(template_path, output_path, year, day)
