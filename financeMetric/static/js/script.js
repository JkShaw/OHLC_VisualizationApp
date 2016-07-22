var app = angular.module('myApp', ['nvd3']);

app.controller('MainCtrl', function($scope, $http) {
    // Stock list come here as drpdown
    var dict = [];
    for(var i=1; i<=10; i++){
        dict.push({
            stockid: i,
            name: 'Stock ' + i
        });
    }
    $scope.stocklist = dict;

    // Stock changed - get stock specific records from db
    $scope.myFunc = function() {

        //Ajax request server to get stock specific records
        $http.get('/getdata', {
            params : { stock: $scope.stockdata.stockid }
        })
        .then(function(response) {
            $scope.options = {
                chart: {
                    type: 'ohlcBarChart',
                    height: 450,
                    margin : {
                        top: 20,
                        right: 20,
                        bottom: 40,
                        left: 60
                    },
                    x: function(d){ 
                        return d3.time.format('%Y-%m-%d').parse(d['date']);
                    },
                    y: function(d){ return d['close']; },
                    useInteractiveGuideline: true,
                    duration: 100,
                    
                    xAxis: {
                        axisLabel: 'Dates',
                        tickFormat: function(d) {
                            return d3.time.format('%Y-%m-%d')(new Date(d));
                        },
                        showMaxMin: false
                    },

                    yAxis: {
                        axisLabel: 'Stock Price',
                        tickFormat: function(d){
                            return '$' + d3.format(',.2f')(d);
                        },
                        showMaxMin: false
                    },
                    zoom: {
                        enabled: true,
                        scaleExtent: [1, 10],
                        useFixedDomain: false,
                        useNiceScale: false,
                        horizontalOff: false,
                        verticalOff: true,
                        unzoomEventType: 'dblclick.zoom'
                    }
                }
            };
            $scope.data = [{values: response.data}];
        });
    }
});
