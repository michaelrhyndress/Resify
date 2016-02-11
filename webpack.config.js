var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

<<<<<<< HEAD
var atImport = require('postcss-import');
var bemLinter = require('postcss-bem-linter');
var autoprefixer = require('autoprefixer');

var __staticDir = path.join(__dirname, "static/assets")

var __bundelDir = path.join(__staticDir, "bundles/")
var __bundleURL = "static/assets/bundles/"

=======
// var atImport = require('postcss-import');
// var bemLinter = require('postcss-bem-linter');
// var autoprefixer = require('autoprefixer');

var __staticDir = path.join(__dirname, "static/assets")

var __bundelDir = path.join(__staticDir, "bundles", "/")
var __bundleURL = "static/assets/bundles/"
var __scssDir = path.join(__staticDir, "scss");
var __scriptDir = path.join(__staticDir, "js");
>>>>>>> oldish-state
module.exports = {
	context: __dirname,

	entry: {
<<<<<<< HEAD
		base: path.join(__staticDir, "react/modules/Base/base"),
		homepage: path.join(__staticDir, "react/modules/Homepage/homepage"),
		registration: path.join(__staticDir, "react/modules/Registration/registration"),
		dashboard: path.join(__staticDir, "react/modules/ResumeDash/dashboard"),
		setup: path.join(__staticDir, "react/modules/InitSetupResume/initSetupResume")
=======
		base: [
			path.join(__staticDir, "react/modules/Base/base"),
		],
		homepage: path.join(__staticDir, "react/modules/Homepage/homepage"),
		registration: path.join(__staticDir, "react/modules/Registration/registration"),
		dashboard: path.join(__staticDir, "react/modules/ResumeDash/dashboard"),
		setup: path.join(__staticDir, "react/modules/InitSetupResume/initSetupResume"),
		vendor: [
			path.join(__staticDir, "js/vendor/jquery-2.1.4.js"),
			"underscore"
		],
>>>>>>> oldish-state
	},

	output: {
		path: __bundelDir,
		publicPath: __bundleURL,
		filename: "[name].bundle.js" //[name]-[hash].js
	},

	plugins: [
		new BundleTracker({filename: './webpack-stats.json'}),
<<<<<<< HEAD
		new webpack.ProvidePlugin({
		    "_": "underscore",
			$: "jquery",
			// jQuery: "jquery"
		}),
		// new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js', Infinity)
=======
		new webpack.optimize.CommonsChunkPlugin(
			"vendor", "vendor.bundle.js", Infinity
		),
		// new webpack.ProvidePlugin({
		//     "_": "underscore",
		// 	$: "jquery",
		// 	jQuery: "jquery",
		// 	"window.jQuery": "jquery"
		// }),
		new webpack.ProvidePlugin({
		    $: "jquery",
		    jQuery: "jquery",
		    "window.jQuery": "jquery",
		}),
		new webpack.optimize.CommonsChunkPlugin(
			"vendor", "vendor.bundle.js", Infinity
		),
		// new webpack.optimize.CommonsChunkPlugin(
		// 	'vendor', 'vendor.bundle.js', Infinity
		// ),
		// new webpack.optimize.UglifyJsPlugin({
		//       		minimize: true,
		//       		compress: {
		//         		warnings: false
		//       		}
		//     	})
>>>>>>> oldish-state
		  
	],

	module: {
		loaders: [
			{ test: /\.js[x]?$/,
				exclude: /node_modules/,
				loader: 'babel',
				query:
				{
					presets:['react']
				}
			}, // to transform JSX into JS
			{
				test: /\.css$/, // Only .css files
				loader: 'style-loader!css-loader!resolve-url' // Run both loaders
			},
			{
				test: /\.scss$/, // Only .css files
				loader: "style!css!resolve-url!sass?sourceMap" // Run both loaders
			},
			{ 
				//file-loader?name=[hash].[ext]!
				test: /\.(png|jpg|gif)$/,
				loader: 'url-loader?limit=8192'
			},
			{ 
				test: /\.(webm|mp4)$/,
				loader: 'file-loader?name=[hash].[ext]'
			},
			{
<<<<<<< HEAD
=======
				test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
				loader: "url-loader",
				query: {
					limit: 10000,
					mimetype: "application/font-woff",
					// name: "[name].[ext]"
				}
			},
			{ // FONTS 
				test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
				loader: "file-loader",
				// query: {
				// 	name: "[name].[ext]"
				// }
			},
			{
>>>>>>> oldish-state
				test: /[\\\/]bower_components[\\\/]modernizr[\\\/]modernizr\.js$/,
				loader: "imports?this=>window!exports?window.Modernizr" 
			}
		],
<<<<<<< HEAD
		postcss: [
		    atImport(),
		    autoprefixer(),
		    bemLinter('bem')
		  ],
	},
	
	sassLoader: {
		includePaths: [path.join(__staticDir, "/scss/")]
	},
	
	resolve: {
		modulesDirectories: ['node_modules'],
=======
		// postcss: [
		//     atImport(),
		//     autoprefixer(),
		//     bemLinter('bem')
		//   ],
	},
	
	sassLoader: {
		includePaths: [__scssDir]
	},
	
	resolve: {
		modulesDirectories: [
			'node_modules',
			__scssDir,
			__scriptDir
		],
>>>>>>> oldish-state
		alias: {
			jquery: path.join(__staticDir, "js/vendor/jquery-2.1.4.js"),
			vide: path.join(__staticDir, "js/vendor/vide.js"),
		},
		extensions: ['', '.js', '.jsx'],
	},
}