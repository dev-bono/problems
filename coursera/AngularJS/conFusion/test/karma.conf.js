module.exports = function(config) {
	config.set({
		basePath: '../',
		frameworks: ['jasmine'],
		// list of files, 테스트하려는 파일 목록
		files: [
			'bower_components/angular/angular.js',
			'bower_components/angular-resource/angular-resource.js',
			'bower_components/angular-ui-router/release/angular-ui-router.js',
			'bower_components/angular-mocks/angular-mocks.js',
			'app/scripts/*.js',
			'test/unit/**/*.js'
		],
		// list of files to exclude, 테스트 제외 목록
		exclude: [
			'test/protractor.conf.js', 'test/e2e/*.js'
		],
		preprocessors: {

		},
		// test results reporter to use
		// possible values: 'dots', 'progress'
		reporters: ['progress'],
		port: 9876,
		// colors in the output (reporters and logs)
		colors: true,
		// config.LOG_DISALBE || config.LOG_ERROR || config.LOG_WARN || config.LOG_INFO || config.LOG_DEBUG
		logLevel: config.LOG_INFO,
		// 파일 변경시 auto reload
		autoWatch: true,
		// browser, available browser launchers
		browsers: ['Chrome', 'PhantomJS', 'PhantomJS_custom'],
		customLaunchers: {
			'PhantomJS_custom': {
				base: 'PhantomJS',
				options: {
					windowName: 'my-window',
					settings: {
						webSecurityEnabled: false
					},
				},
				flags: ['--load-images=true'],
				debug: true
			}
		},
		phantomjsLauncher: {
			// ResourceError 발생시 phantomjs 종료, 비정상 종료시 유용함
			exitOnResourceError: true
		},
		// Continuous Integration mode
		// if true, Karma captures browsers, runs the tests and exits
		singleRun: false,
		// Concurrency level
		concurrency: Infinity

	})
}