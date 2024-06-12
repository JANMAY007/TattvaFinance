const CACHE_NAME = 'ttf-cache-v1';
const urlsToCache = [
  '',
  '/offline',
  '/static/Logo/logo.png',
];

// Install service worker and cache the static assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// Fetch event to serve cached assets
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Return cached asset or fetch from network
        return response || fetch(event.request);
      })
      .catch(() => {
        // Fallback to offline.html for navigation requests
        if (event.request.mode === 'navigate') {
          return caches.match('/offline');
        }
      })
  );
});

// Activate service worker and remove old caches
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (!cacheWhitelist.includes(cacheName)) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
