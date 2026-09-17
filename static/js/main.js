// =========================================
// MOBILE NAVIGATION
// =========================================

const mobileMenuButton = document.getElementById("mobileMenuButton");

const navLinks = document.getElementById("navLinks");

if (mobileMenuButton && navLinks) {
  mobileMenuButton.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("active");

    mobileMenuButton.setAttribute("aria-expanded", isOpen);

    mobileMenuButton.innerHTML = isOpen ? "✕" : "☰";
  });

  // Close menu when a link is clicked

  const navItems = navLinks.querySelectorAll("a");

  navItems.forEach((item) => {
    item.addEventListener("click", () => {
      navLinks.classList.remove("active");

      mobileMenuButton.setAttribute("aria-expanded", "false");

      mobileMenuButton.innerHTML = "☰";
    });
  });
}

/* =========================================
   MENU FILTER
========================================= */

const categoryButtons = document.querySelectorAll(".category-button");

const menuCards = document.querySelectorAll(".menu-card");

categoryButtons.forEach((button) => {
  button.addEventListener("click", () => {
    /*
                Remove active class
                from all buttons
            */

    categoryButtons.forEach((btn) => {
      btn.classList.remove("active");
    });

    /*
                Activate clicked button
            */

    button.classList.add("active");

    /*
                Get selected category
            */

    const selectedCategory = button.dataset.category;

    /*
                Filter menu cards
            */

    menuCards.forEach((card) => {
      const cardCategory = card.dataset.category;

      if (selectedCategory === "all" || selectedCategory === cardCategory) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  });
});

/* =========================================
   GALLERY FILTER
========================================= */

const galleryFilters = document.querySelectorAll(".gallery-filter");

const galleryItems = document.querySelectorAll(".gallery-item");

galleryFilters.forEach((filter) => {
  filter.addEventListener("click", () => {
    galleryFilters.forEach((button) => {
      button.classList.remove("active");
    });

    filter.classList.add("active");

    const selectedFilter = filter.dataset.filter;

    galleryItems.forEach((item) => {
      const category = item.dataset.category;

      if (selectedFilter === "all" || category === selectedFilter) {
        item.style.display = "block";
      } else {
        item.style.display = "none";
      }
    });
  });
});

/* =========================================
   GALLERY LIGHTBOX
========================================= */

const lightbox = document.getElementById("lightbox");

const lightboxImage = document.getElementById("lightboxImage");

const lightboxTitle = document.getElementById("lightboxTitle");

const lightboxClose = document.getElementById("lightboxClose");

const lightboxPrev = document.getElementById("lightboxPrev");

const lightboxNext = document.getElementById("lightboxNext");

let currentGalleryIndex = 0;

function getVisibleGalleryItems() {
  return Array.from(galleryItems).filter((item) => {
    return item.style.display !== "none";
  });
}

function openLightbox(item) {
  const visibleItems = getVisibleGalleryItems();

  currentGalleryIndex = visibleItems.indexOf(item);

  showGalleryImage();

  lightbox.classList.add("active");

  document.body.style.overflow = "hidden";
}

function showGalleryImage() {
  const visibleItems = getVisibleGalleryItems();

  if (!visibleItems.length) {
    return;
  }

  const item = visibleItems[currentGalleryIndex];

  lightboxImage.src = item.dataset.image;

  lightboxImage.alt = item.dataset.title;

  lightboxTitle.textContent = item.dataset.title;
}

galleryItems.forEach((item) => {
  item.addEventListener("click", () => {
    openLightbox(item);
  });
});

function closeLightbox() {
  lightbox.classList.remove("active");

  document.body.style.overflow = "";
}

function showNextImage() {
  const visibleItems = getVisibleGalleryItems();

  currentGalleryIndex = (currentGalleryIndex + 1) % visibleItems.length;

  showGalleryImage();
}

function showPreviousImage() {
  const visibleItems = getVisibleGalleryItems();

  currentGalleryIndex =
    (currentGalleryIndex - 1 + visibleItems.length) % visibleItems.length;

  showGalleryImage();
}

if (lightboxClose) {
  lightboxClose.addEventListener("click", closeLightbox);
}

if (lightboxNext) {
  lightboxNext.addEventListener("click", showNextImage);
}

if (lightboxPrev) {
  lightboxPrev.addEventListener("click", showPreviousImage);
}

if (lightbox) {
  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox) {
      closeLightbox();
    }
  });
}

document.addEventListener("keydown", (event) => {
  if (!lightbox || !lightbox.classList.contains("active")) {
    return;
  }

  if (event.key === "Escape") {
    closeLightbox();
  }

  if (event.key === "ArrowRight") {
    showNextImage();
  }

  if (event.key === "ArrowLeft") {
    showPreviousImage();
  }
});

// =========================================
// DJANGO MESSAGE AUTO-HIDE
// =========================================

const messageAlerts = document.querySelectorAll(".message-alert");

messageAlerts.forEach((message) => {
  setTimeout(() => {
    message.style.opacity = "0";
    message.style.transform = "translateX(30px)";

    setTimeout(() => {
      message.remove();
    }, 400);
  }, 5000);
});

// =========================================
// CURRENT YEAR
// =========================================

const currentYear =
    document.getElementById("currentYear");

if (currentYear) {

    currentYear.textContent =
        new Date().getFullYear();

}

/* =========================================
   SCROLL REVEAL
========================================= */

const revealElements =
    document.querySelectorAll(".reveal");

const revealObserver =
    new IntersectionObserver(
        (entries) => {

            entries.forEach((entry) => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("active");

                    revealObserver.unobserve(
                        entry.target
                    );
                }

            });

        },
        {
            threshold: 0.15
        }
    );

revealElements.forEach((element) => {

    revealObserver.observe(element);

});