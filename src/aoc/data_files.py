"""Object to hold AoC data files."""

from pathlib import Path


_RELATIVE_BASE_PATH = Path(__file__).parent.parent


class DataFiles:
    """Object to hold data AoC files."""

    def __init__(self, base_path: Path = _RELATIVE_BASE_PATH):
        """Initialize the object."""
        self._base_path = base_path
        self._get_input_files()
        self._get_example_files()

    def _get_input_files(self):
        """Get the input files."""
        input_files = list(self._base_path.glob("**/data/*_input.txt"))
        self.input_files = {}

        for input_file in input_files:
            year = int(input_file.parent.parent.name)
            day = int(input_file.stem[4:].split("_")[0])
            self.input_files[(year, day)] = input_file

    def _get_example_files(self):
        """Get the example files."""
        example_files = list(self._base_path.glob("**/data/*_example*.txt"))
        self.example_files: dict[tuple[int, int], Path | dict[int, Path]] = {}

        for example_file in example_files:
            year = int(example_file.parent.parent.name)
            day = int(example_file.stem[4:].split("_")[0])

            n_files_for_day = len(
                [
                    f
                    for f in example_files
                    if f.stem.startswith(f"day_{day:02}") and f.parent.parent.name == str(year)
                ]
            )

            if n_files_for_day > 1:
                number = int(example_file.stem.split("example_")[1])
                example_list: dict[int, Path] = self.example_files.get((year, day), {})  # type: ignore
                example_list[number] = example_file
                self.example_files[(year, day)] = example_list
            else:
                self.example_files[(year, day)] = example_file

    def show_data_files(self):
        """Show the data files."""
        print("Input files:")
        for key, value in self.input_files.items():
            print(key, value)

        print("\nExample files:")
        for key, value in self.example_files.items():  # type: ignore
            print(key, value)
