"""So Here we Go.

Note:
-  It must have a proper structure following the order 
1. Abstract
2. Introduction
3. Conclusion
4. Reference

- For the citation generation its not going to be like AI generation oooo its going to be like using inputs to get in
the data and make a compilation of it into a document on it's own and done its generated. So we are to align this
genration of a thing in the following Formats: 1. APA 2. MLA 3. Chicago 4. IEEE

- It must be able to check and compare the references of both what is written in the document being checked and
another document where all supposed/included references supposed to be included in the document So it checks and
picks out the ones absent or unused in the document

        SO FAR ARE YOU GUYS GRABBING

- It should be able to determine the writing style in the sense that it tells us in the report on whether long
sentences were included

- It should be able to test for plagiarism in terms of if there were lot or less of similarities between texts or
documents respectively

        AND FINALLY 

- It should be able to deliver a report on the screenings and test that has been done

      AND THAT'S ALL FOR IT YOU SEE ITS SO SIMPLE (sMILEs 😂😂)
      
Now to get down to business
- so guys definitely we are going to have the need to import some libraries because each library will handle
1. Command-line Arguments
2. File handling or directory handling
3. Plagiarism similarity test check
4. Report generation
5. The Availability to terminate a program on an error


AND MOST IMPORTANTLY I'M MAKING IT INTO SOME KIND OF OPTION SCENERIO THAT YOU'LL PICK EITHER PLAGIARISM AND STRUCTURE
TEST OR CITATION TEST"""

# Imports
import argparse
import os
from datetime import datetime
import json
import re


# OverallBase class "like the foundation of all analysis"
class AcademicPaperAnalyzer:
    """This is to initialize some really important element paths for location  detection and others """

    def __init__(self, paper_path, refs_path, container_dir):
        self.paper_path = paper_path
        self.refs_path = refs_path
        self.container_dir = container_dir
        self.paper_text = self._read_file(self.paper_path)
        self.reference_list = self._read_file(self.refs_path).splitlines()

    """This def function is to define a run file/directory file so as for the code to be able to view and read the 
    document saved on it"""

    def _read_file(self, path):
        """Safely read a file with fallback encoding."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            with open(path, 'r', encoding='latin-1') as f:
                return f.read()

        # True definite Analyzers
        # 1. STRUCTURE CHECK

    """This is a def function to check whether the stucture format is in place and complete the abstract, 
    introduction, conclusion and reference"""

    def check_structure(self):
        text = self.paper_text.lower()
        return {
            "abstract": "abstract" in text,
            "introduction": "introduction" in text,
            "conclusion": "conclusion" in text,
            "references_section": "references" in text
        }

    """ while this (sections = ["Abstract", "Introduction", "Conclusion", "References"]
return {sec.lower() in text.lower() for sec in sections} this displays true if all are through"""

    #  2. REFERENCES VALIDATION

    def validate_references(self):
        """Very basic check for missing/unused refs."""
        in_text_citations = re.findall(r"\(([^)]+, \d{4})\)", self.paper_text)  # e.g. (Smith, 2020)
        """This is to determine the references that were wrong and not part of the full original reference bank that 
        was kept for checking"""
        missing_in_refs = [c for c in in_text_citations if c not in self.reference_list]
        """This is to identify the unused references that were not in the original document but present in the 
        reference bank"""
        unused_in_refs = [r for r in self.reference_list if r not in in_text_citations]
        # This is to return the things identified so as to be displayed later on
        return {
            "missing_in_refs": missing_in_refs,
            "unused_in_refs": unused_in_refs
        }

    #  3. WRITING STYLE ANALYSIS
    """Now this one is about the writing style and organization as in long sentences in particular with some 
    additional feautures like avaerage word per seconds and passive count"""

    def analyze_writing_style(self):
        sentences = re.split(r'[.!?]', self.paper_text)
        long_sentences = [s for s in sentences if len(s.split()) > 20]
        passive_count = len(re.findall(r"\b(been|was|were|is|are|be)\b\s+\w+ed", self.paper_text))
        return {
            "long_sentences_count": len(long_sentences),
            "passive_voice_count": passive_count,
            "average_words_per_sentence": round(sum(len(s.split()) for s in sentences if s) / max(1, len(sentences)), 2)
        }

    #  4. PLAGIARISM CHECK
    """As you can see this one is to test for plagiarism"""

    def check_plagiarism(self):
        results = []
        if not os.path.exists(self.container_dir):
            return None
        """This part is to specify that the document it should identify must be in .txt format"""
        for file in os.listdir(self.container_dir):
            if file.endswith(".txt"):
                file_path = os.path.join(self.container_dir, file)
                """while this part is to read the file that has been screened for having using .txt format """
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    container_text = f.read()
            """This shows the display of hoe we want the simlarity and file name to be displayed"""
            similarity = self._calculate_similarity(self.paper_text, container_text)
            results.append({"container_file": file, "similarity": similarity})
        return results

    """while this section is for how the plagiarism really works how it will compare the words from the different 
    document stored in the container bank or directory"""

    def _calculate_similarity(self, text1, text2):
        """Very simple similarity metric (common words)."""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        if not words1 or not words2:
            return 0.0
        return round(len(words1 & words2) / len(words1 | words2), 2)

    # File Handling

    # RUN ALL ANALYSIS
    """Now this is the highlight of all the keys needed to be displayed as our report"""

    def run_all(self):
        return {
            "structure": self.check_structure(),
            "references": self.validate_references(),
            "style": self.analyze_writing_style(),
            "plagiarism": self.check_plagiarism()
        }

    """Now this aspect shows how the report will be stored and treansfered into a json file after a few automation in 
    code"""


def save_report(report, output):
    """Append new report to JSON file safely."""
    if os.path.exists(output):
        try:
            with open(output, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []
    """This area is for how when we keep on test running and adding more reports into the file instead of the json 
    document created to be replacing the old one i decided that how about it just keeps on appending as tho its in a 
    list Array like to be grouped differently"""
    if not isinstance(data, list):
        data = [data]
    data.append(report)
    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Report saved to {output}")


"""Citation Generation"""


class CitationGenerator:
    """Generates formatted citations for APA, MLA, Chicago, and IEEE."""

    def __init__(self, author, year, title, journal, volume=None, pages=None):
        """This aspect is to highlight the details that form up a citation the author, year, title, journal, volume,
        pages"""
        self.author = author
        self.year = year
        self.title = title
        self.journal = journal
        self.volume = volume
        self.pages = pages

    """Now this aspect is to define how each type of citation format should arrange the author, year, volume..... etc"""

    def apa(self):
        """Generate APA style citation."""
        return f"{self.author} ({self.year}). {self.title}. {self.journal}, {self.volume}, {self.pages}."

    def mla(self):
        """Generate MLA style citation."""
        return f"{self.author}. \"{self.title}.\" {self.journal}, vol. {self.volume}, {self.year}, pp. {self.pages}."

    def chicago(self):
        """Generate Chicago style citation."""
        return f"{self.author}. \"{self.title}.\" {self.journal} {self.volume} ({self.year}): {self.pages}."

    def ieee(self):
        """Generate IEEE style citation."""
        return f"{self.author}, \"{self.title},\" {self.journal}, vol. {self.volume}, pp. {self.pages}, {self.year}."

    def run_citation(self):
        return {
            "APA format": self.apa(),
            "MLA format": self.mla(),
            "Chicago": self.chicago(),
            "IEEE": self.ieee()
        }

    """Now this aspect shows how the report will be stored and treansfered into a json file after a few automation in 
    code"""


def save_Citstion_report(report, output):
    """Append new report to JSON file safely."""
    if os.path.exists(output):
        try:
            with open(output, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []
    """This area is for how when we keep on test running and adding more reports into the file instead of the json 
        document created to be replacing the old one i decided that how about it just keeps on appending as tho its in a 
        list Array like to be grouped differently"""
    if not isinstance(data, list):
        data = [data]
    data.append(report)
    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Report saved to {output}")


"""Hope you guys have been understanding all this from when we started"""


def activate():
    print(f"\n       DOCUMENT ANALYSIS, PLAGIARISM TEST AND CITATION GENERATOR")
    print(f"\n")
    print(f"1. Document Analysis, Plagiarism and Report Generation")
    print(f"2. Citation Generator")
    choice = int(input("Which option are you going for: "))

    def main():
        """Analysis Main"""
        # define the command line arguments and to direct the code to where the file to be tested resides at
        parser = argparse.ArgumentParser(description="Academic Paper Analysis CLI Tool")
        parser.add_argument("--paper",
                            help="C:\\Users\\PEACE\\Desktop\\Academic Document Analysis and Generation\\Robotics.txt")  # Path to the paper text file

        parser.add_argument("--refs",
                            help="C:\\Users\\PEACE\\Desktop\\Academic Document Analysis and Generation\\Reference.txt")

        parser.add_argument("--container_dir",
                            help="C:\\Users\\PEACE\\Desktop\\Academic Document Analysis and Generation\\container")

        parser.add_argument("--output", default="Document Analysis report.json", help="Analysis Report")
        args = parser.parse_args()

        """So after giving it a directory to where the file is so i decided that if the file can't be found directly 
        i'll make a backup to input the directory itself when the code is being run"""
        if not any([args.paper, args.refs, args.container_dir]):
            print("\n No file path provided switching to Interactive Mode..\n")
            args.paper = input(f"Enter path to your document file (e.g.. "
                               f"C:\\Users\\PEACE\\Desktop\\Academic Document Analysis and Generation\\Robotics.txt): ").strip()
            args.refs = input(f"Enter path to your compiled references file (e.g.. "
                              f"C:\\Users\\PEACE\\Desktop\\Academic Document Analysis and Generation\\Reference.txt): ").strip()
            args.container_dir = input(f"Enter path to your container folder (e.g.. "
                                       f"C:\\Users\\PEACE\\Desktop\\Academic Document Analysis and "
                                       f"Generation\\container): ").strip()
        # ✅ RUN ANALYSIS
        analyzer = AcademicPaperAnalyzer(args.paper, args.refs, args.container_dir)
        report = analyzer.run_all()
        # ✅ Add timestamp to report for clarity
        """This area here is the automation of any moment we save the file its keeps a date and time record of when 
        we added to the file"""
        report["analyzed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ✅ SAVE REPORT
        save_report(report, args.output)

    """Citation Main"""

    def gain():
        print("Citation Generator Tool")
        print("Fill in the details below:\n")
        """This is to input each of the citation element """
        # Collect user inputs
        author = input("Author (Lastname, Initials): ")
        year = input("Year: ")
        title = input("Title of article/book: ")
        journal = input("Journal/Book Title: ")
        volume = input("Volume (optional): ")
        pages = input("Pages (optional): ")

        # Generate citations
        citation = CitationGenerator(author, year, title, journal, volume, pages)
        print("\n✅ Generated Citations:")
        print("-" * 50)
        print(f"APA: {citation.apa()}")
        print(f"MLA: {citation.mla()}")
        print(f"Chicago: {citation.chicago()}")
        print(f"IEEE: {citation.ieee()}")
        print("-" * 50)

        """This is to also make it also save to a json file"""
        parser = argparse.ArgumentParser(description="Citation generator CLI Tool")
        parser.add_argument("--output", default="Citation report.json", help="Analysis Report")
        args = parser.parse_args()

        citation_analysis = CitationGenerator(author, year, title, journal, volume, pages)
        report = citation_analysis.run_citation()
        # ✅ Add timestamp to report for clarity
        """This area here is the automation of any moment we save the file its keeps a date and time record of when 
        we added to the file"""
        report["analyzed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_report(report, args.output)

    """I created this spot here to make it into an option choosing scenerio program"""
    if choice == 1:
        print(main())
    elif choice == 2:
        print(gain())
    else:
        print(f'\n Make a Choice')


# this is to call or activate the def function  or in short run the code
activate()
print(activate())
