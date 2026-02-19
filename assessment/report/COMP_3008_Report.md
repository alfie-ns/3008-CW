---
title: "COMP3008: Report (...)"
header-includes:
  - \usepackage{graphicx}
  - \usepackage{caption}
  - \usepackage{tikz}
  - \usetikzlibrary{positioning, arrows.meta}
  - \usepackage{xcolor}
  - \usepackage{float}
  - \usepackage{array}
  - \usepackage{tabularx}
  - \usepackage{mdframed}
  - \usepackage{booktabs}
  - \usepackage{pgfplots}
  - \pgfplotsset{compat=1.18}
  - \usepackage{listings}
  - \usepackage{hyperref}
  - \usepackage{multirow}
  - |
      \lstset{
        language=Matlab,
        numbers=left,
        breaklines=true,
        breakatwhitespace=true,
        postbreak=\mbox{\textcolor{gray}{$\hookrightarrow$}\space},
        basicstyle=\ttfamily\small,
        columns=flexible,
        escapeinside={(*@}{@*)},
        showstringspaces=false
      }
---
# TODO
- [ ] “expectation-maximisation’ algorithm when imputing missing data 
- [ ] ‘missingness’ 
- [ ] ‘concluding’
- [ ] ‘effectively’
- [ ] and thus, it is asymptotically unbiased 
- [ ] principle components (missing-data lecture)
- [ ] don’t copy Lauren’s stuff just imitate her lecture words etc
- [ ] deal with missing data in the code and comment to talk about this 
- [ ] 

- [ ] utilise lecture transcripts 

- [ ] heavily talk about the underlying maths of the code via latex

- [ ] ensure the plots look very distinct like I put a lot of time in changing how it looks eg colours
- [ ] in the code remove any spaces that are not needed 
- [ ] Don't use Word Clouds for Categorical Data
- [ ] no pie, 3D, radar charts
- [ ] Lauren does not care about the code but the analysis
- [ ] derive Lauren’s coding conventions from her GitHub 
- [ ] latex AND python visualtions derived for lecture 6. Line graph !! Lauren wants this, ensure is clear if needed vote lec 6
- [ ] args and kwargs
- [ ] concise-as-possible alike COMP_3003
- [ ] LaTeX diagram that has fully context within cw
- [ ] rember to utilise the `lecture-notes.md` from ALL the relevant lectures, dynamically whilst making the coursework
- [ ] Go as far as conceptually as possible, as far complex as the subject goes
- [ ] Make the code work ASAP and start talking about it using what's learnt in the module via Lauren

# Appendices

## Appendix A: ...

## Appendix B: 5-Minute Video Demo

- YouTube link: [test](test)

## Appendix C: AI Declaration

\begin{figure}[H]
\centering
\includegraphics[width=0.55\textwidth]{image/ai-decl.png}
\caption{Student Declaration of AI Tool use in this Assessment Table}
\end{figure}

I declare that I've used the AI tools listed below whilst preparing this assessment. I've read and understood the University of Plymouth's policy on the use of AI tools in assessment and confirm that my use falls within the coursework's allowed categories, i.e. \textbf{A2 (Planning and Structuring Projects)} and \textbf{A4 (Research Assistance)}.

\renewcommand{\arraystretch}{1.1}
\setlength{\tabcolsep}{4pt}

\begin{tabular}{|>{\raggedright\arraybackslash}p{3.2cm}|
                >{\raggedright\arraybackslash}p{8cm}|
                >{\raggedright\arraybackslash}p{4cm}|}
\hline
\textbf{AI Tool Used} & \textbf{Purpose of Use} & \textbf{Extent of Use} \\
\hline
ChatGPT & Finding relevant pages to read in the paper \textbf{(A4)} & Few times if the paper is too long \\
\hline
ChatGPT & General conversations via web-search AI about prevalent papers to read about how the topics relates to others' studies \textbf{(A4)} & Few times at the end \\
\hline
\end{tabular}

- [X] I understand that the ownership and responsibility for the academic integrity of this submitted assessment falls with me, the student.
- [X] I confirm that all details provide above are an accurate description of how AI was used for this assessment.
