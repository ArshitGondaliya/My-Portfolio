document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  const progress = document.querySelector('.scroll-progress');
  const typedText = document.querySelector('.typed-text');
  const phrases = ['Software Engineer', 'Web Developer', 'Data Analytics Enthusiast', 'Machine Learning Learner'];
  let phraseIndex = 0;
  let characterIndex = phrases[0].length;
  let deleting = true;

  menuToggle?.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', String(isOpen));
    menuToggle.innerHTML = `<i class="fa-solid fa-${isOpen ? 'xmark' : 'bars'}"></i>`;
  });

  navLinks?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    menuToggle?.setAttribute('aria-expanded', 'false');
    if (menuToggle) menuToggle.innerHTML = '<i class="fa-solid fa-bars"></i>';
  }));

  const typePhrase = () => {
    if (!typedText) return;
    const phrase = phrases[phraseIndex];
    if (deleting) characterIndex -= 1;
    else characterIndex += 1;
    typedText.textContent = phrase.slice(0, characterIndex);
    let delay = deleting ? 42 : 82;
    if (!deleting && characterIndex === phrase.length) { deleting = true; delay = 1500; }
    if (deleting && characterIndex === 0) { deleting = false; phraseIndex = (phraseIndex + 1) % phrases.length; delay = 320; }
    window.setTimeout(typePhrase, delay);
  };
  window.setTimeout(typePhrase, 1600);

  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) entry.target.classList.add('revealed');
  }), { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));

  const sections = [...document.querySelectorAll('main section[id], header[id]')];
  const navItems = [...document.querySelectorAll('.nav-links a')];
  const sectionObserver = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) navItems.forEach((item) => item.classList.toggle('active', item.getAttribute('href') === `#${entry.target.id}`));
  }), { rootMargin: '-35% 0px -55% 0px' });
  sections.forEach((section) => sectionObserver.observe(section));

  window.addEventListener('scroll', () => {
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = `${scrollHeight > 0 ? (window.scrollY / scrollHeight) * 100 : 0}%`;
  }, { passive: true });

  const filterButtons = document.querySelectorAll('.filter-button');
  const projectCards = document.querySelectorAll('.project-card');
  filterButtons.forEach((button) => button.addEventListener('click', () => {
    filterButtons.forEach((item) => item.classList.remove('active'));
    button.classList.add('active');
    const filter = button.dataset.filter;
    projectCards.forEach((card) => card.classList.toggle('is-hidden', filter !== 'all' && card.dataset.category !== filter));
  }));

  const modal = document.querySelector('.modal');
  const closeModal = () => { modal?.classList.remove('open'); modal?.setAttribute('aria-hidden', 'true'); document.body.style.overflow = ''; };
  document.querySelectorAll('.project-open').forEach((button) => button.addEventListener('click', () => {
    const data = document.getElementById(button.dataset.project);
    if (!data || !modal) return;
    modal.querySelector('.modal-title').textContent = data.dataset.title;
    modal.querySelector('.modal-category').textContent = data.dataset.category;
    modal.querySelector('.modal-description').textContent = data.dataset.description;
    modal.querySelector('.modal-tech').innerHTML = data.dataset.technologies.split(',').map((tech) => `<span>${tech.trim()}</span>`).join('');
    const actions = modal.querySelector('.modal-actions');
    actions.innerHTML = '';
    if (data.dataset.github) actions.innerHTML += `<a class="button button-primary" href="${data.dataset.github}" target="_blank" rel="noreferrer">GitHub <i class="fa-brands fa-github"></i></a>`;
    if (data.dataset.demo) actions.innerHTML += `<a class="button button-ghost" href="${data.dataset.demo}" target="_blank" rel="noreferrer">Live demo <i class="fa-solid fa-arrow-up-right-from-square"></i></a>`;
    modal.classList.add('open'); modal.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden';
  }));
  document.querySelector('.modal-close')?.addEventListener('click', closeModal);
  document.querySelector('.modal-backdrop')?.addEventListener('click', closeModal);
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape') closeModal(); });
});
