var kalpavrukshApp = angular.module("kalpavrukshApp", [
	'ui-notification',
    'angular-loading-bar',
]);

kalpavrukshApp.config(['NotificationProvider', '$httpProvider', function(NotificationProvider, $httpProvider) {

    NotificationProvider.setOptions({
        delay: 3000,
        startTop: 20,
        startRight: 10,
        verticalSpacing: 20,
        horizontalSpacing: 20,
        positionX: 'right',
        positionY: 'top'
    });

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

}]);

kalpavrukshApp.controller("kalpavrukshControllers", ['$scope', '$log', '$http','$timeout', function($scope, $log, $http, $timeout) {
	console.log("kalpavrukshControllers loads");

     $scope.date = new Date();

	var getDashboardSummary = function(requestObj) {
        $http.post('/dashboard_data/').
        success(function(data, status, headers, config) {
        	console.log(data);
        	$scope.data = data;
        }).
        error(function(data, status, headers, config) {
            console.log(data);
        });
    }

    getDashboardSummary();

}]);