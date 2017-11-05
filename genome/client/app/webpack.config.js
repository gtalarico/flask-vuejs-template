var path = require('path')
var webpack = require('webpack')
var FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin')

module.exports = {
  entry: './src/main.js',
  output: {
    path: path.resolve(__dirname, './dist'),
    publicPath: '/dist/',
    // publicPath: '/dist/',
    filename: 'build.js'
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        loader: 'css-loader!sass-loader',
        exclude: /node_modules/
      },
      {
        test: /\.sass$/,
        loader: 'sass-loader?indentedSyntax=1',
        exclude: /node_modules/
      },
      {
        test: /\.css$/,
        loader: 'css-loader!css!style!',
        exclude: /node_modules/
      },
      {
        // Lint local *.vue files
        enforce: 'pre',
        test: /\.vue$/,
        loader: 'eslint-loader',
        exclude: /node_modules/
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
            // 'scss': 'vue-style-loader!css-loader!sass-loader',
            'scss': 'vue-style-loader!css-loader!sass-loader&data=@import "./src/assets/sass/main.sass"',
            // 'sass': 'vue-style-loader!css-loader!sass-loader?indentedSyntax=1',
            'sass': 'vue-style-loader!css-loader!sass-loader?indentedSyntax=1&data=@import "./src/assets/sass/main.sass"'
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      },
    ]
  },
  resolve: {
    extensions: ['.js', '.vue', '.json', '.css', 'scss'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    }
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    quiet: true // Off, Using FriendlyErrorsPlugin
  },
  performance: {
    hints: false
  },
  // devtool: '#eval-source-map',
  devtool: '#eval-cheap-module-source-map',
  plugins: [
    new FriendlyErrorsPlugin()
  ]
}


if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}
