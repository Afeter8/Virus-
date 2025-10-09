const domainRotator = {
  activeDomains: [
    'tpb.party',
    'thepiratebay.org',
    'piratebayproxy.info'
  ],
  getRandomDomain: function() {
    return this.activeDomains[Math.floor(Math.random() * this.activeDomains.length)];
  }
};
