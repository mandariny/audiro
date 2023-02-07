const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://i8a402.p.ssafy.io:8080',
      changeOrigin: true,
    })
  );
};