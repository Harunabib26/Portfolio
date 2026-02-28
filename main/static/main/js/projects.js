// Projects Data
const projects = [
    {
        title: "AgricConnect",
        impact: "Connecting Farmers to Markets",
        description: "A digital multi-vendor platform for agricultural services. Built to solve supply chain delays.",
        stack: ["Python", "MySQL", "Flask", "Tailwind"],
        demo: "#",
        github: "#",
        image: "assets/images/agric-connect.jpg"
    },
    {
        title: "EstateManager Pro",
        impact: "Aiding Real Estate Operations",
        description: "Comprehensive system for property management, automated tenant billing, and maintenance tracking.",
        stack: ["Python", "Django", "PostgreSQL"],
        demo: "#",
        github: "#",
        image: "assets/images/hero-bg.png" // Placeholder
    },
    {
        title: "TailorTrack",
        impact: "Digitalizing Bespoke Fashion",
        description: "Measurement management and order tracking system for high-end tailoring businesses.",
        stack: ["HTML", "CSS", "JS", "SQLite"],
        demo: "#",
        github: "#",
        image: "assets/images/hero-bg.png" // Placeholder
    },
    {
        title: "QuickBill",
        impact: "Simplified Business Invoicing",
        description: "A lightweight desktop tool for generating professional receipts and tracking daily sales.",
        stack: ["Python", "Tkinter", "MySQL"],
        demo: "#",
        github: "#",
        image: "assets/images/hero-bg.png" // Placeholder
    }
];

function renderProjects() {
    const grid = document.getElementById('projectsGrid');
    if (!grid) return;

    // Clear existing (except maybe the first hardcoded one if we want to keep it as template)
    grid.innerHTML = '';

    projects.forEach(project => {
        const card = document.createElement('article');
        card.className = 'project-card';
        card.innerHTML = `
            <div class="project-img" style="background: linear-gradient(rgba(15, 23, 42, 0.7), rgba(15, 23, 42, 0.7)), url('${project.image}'); background-size: cover; background-position: center;">
                <div style="height: 100%; display: flex; align-items: center; justify-content: center; opacity: 0.1;">
                    <i data-lucide="layout" size="48"></i>
                </div>
            </div>
            <div class="project-content">
                <h3>${project.title}</h3>
                <p class="project-impact">${project.impact}</p>
                <p class="project-description">${project.description}</p>
                <div class="project-stack">
                    ${project.stack.map(tech => `<span class="skill-tag">${tech}</span>`).join('')}
                </div>
                <div class="project-links">
                    <a href="${project.demo}" class="btn btn-secondary btn-sm" style="padding: 0.4rem 1rem; font-size: 0.8rem;">Live Demo</a>
                    <a href="${project.github}" class="btn btn-secondary btn-sm" style="padding: 0.4rem 1rem; font-size: 0.8rem;"><i data-lucide="github" style="width: 16px; height: 16px;"></i></a>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });

    // Re-initialize icons for dynamic content
    if (window.lucide) {
        lucide.createIcons();
    }
}

document.addEventListener('DOMContentLoaded', renderProjects);
