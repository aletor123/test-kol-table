var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var VueLoader = require('vue-loader')

module.exports = {
  context: __dirname,

  entry: './assets/js/index', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs

  output: {
      path: path.resolve('./assets/webpack_bundles/'),
      filename: "[name]-[fullhash].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new VueLoader.VueLoaderPlugin(),
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        // Exclude transpiling `node_modules`, except `bootstrap-vue/src`
        exclude: /node_modules\/(?!bootstrap-vue\/src\/)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      },
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.vue$/i,
        use: {
          loader: 'vue-loader',
          options: {
            js: 'babel-loader!eslint-loader'
          }
        }
      },
    ]
  },

  resolve: {
    alias: {
      // Alias for using source of BootstrapVue
      vue$: 'vue/dist/vue.runtime.esm.js'
    },
    modules: ['node_modules', 'bower_components'],
    extensions: ['.js', '.jsx']
  },
}