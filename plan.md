# Plan for "Geotechnical and Structural Analyses of Barrettes"

## Main Plan
Create a guide to geotechnical and structural analyses of barrettes (rectangular deep foundation elements). Focus on theoretical foundations, practical design methods, and code-based approaches.

**Target Audience**: Geotechnical and structural engineers, engineering students.

## Rules for Creating the Resource

1. **Accuracy**: Base content on established engineering principles and recognized codes/standards
2. **Clarity**: Explain concepts clearly with diagrams and examples
3. **Citations**: Reference authoritative sources (codes, textbooks, papers)
4. **Mathematical Rigor**: Include relevant equations with clear notation and SI units

## Main Resource Sections

- **Introduction**: Definition, applications, advantages/limitations
- **Geotechnical Analysis**: Bearing capacity, settlement, soil-structure interaction, lateral resistance
- **Structural Analysis**: Axial loads, bending/shear, reinforcement design, connections
- **Case Studies**: Real-world projects and lessons learned
- **Conclusion**: Summary, best practices, references

## File Structures

```
resources/
??? 01-introduction/
??? 02-geotechnical-analysis/
??? 03-structural-analysis/
??? 04-case-studies/
??? 05-conclusion/
??? appendix/
??? figures/          # All figures and diagrams
??? papers/           # Research papers
??? textbooks/        # Textbook references
??? documentation/    # Additional documentation
```

## Main Rules and Format

1. **File Structure**: Each section should be in its own file
2. **Format**: All files are Markdown (.md)
3. **Equations**: LaTeX format required:
   - Math samples inline: use single dollar signs (`$P_u = q_u \times A$`)
   - Equations standalone: use double dollar signs (`$$...$$`) on their own line with no text before or after
   - Equations can span multiple lines for matrices and complex expressions
1. **Resources Folder**: All documentation, figures, research papers, and textbooks should be stored in the `resources/` folder
2. **Citations**: Use author-year format (e.g., `[Author, Year]` or `(Author, Year)`) with full references listed at end
3. **Figures**: Store figures in `resources/figures/` directory
4. **Units**: SI units (metric) primary
5. **Terminology**: Consistent throughout
6. **Headings**: Use hierarchical headings (H1 for title, H2 for sections, H3 for subsections)
7. **Tables**: Use markdown table syntax with clear headers
8. **Cross-references**: Use relative links to other sections/files for navigation
9. **Language**: Clear, professional English with technical precision

