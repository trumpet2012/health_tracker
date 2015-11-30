function create_profile_charts(profile_id) {
    $.ajax({
        url: "http://localhost:8000/profile-api/" + profile_id + "/",
        dataType: "json",
        success: function (json) {
            //Catch errors
            if (!json || json.Message) {
                console.error("Error: " + json.Message);
                return;
            }
            show_eating_info(json);
            show_exercise_info(json);
            //show_weight_info(json);
        },
        error: function (response, txtStatus) {
            console.log(response, txtStatus)
        }
    });

    function show_eating_info(json) {
        var breakfastSeries = [];
        var lunchSeries = [];
        var dinnerSeries = [];

        var days_used = [];

        var records = json['records'];
        $.each(records, function (index, record) {
            var eating_info = record['eating_info'];
            $.each(eating_info, function (index, eat) {
                var meal_time = eat.meal_time;
                if (eat.calories) {
                    var data_point = [
                        record.activity_date,
                        eat.calories
                    ];

                    days_used.push(record.activity_date);

                    if (meal_time == 'breakfast') {
                        breakfastSeries.push(data_point);
                    }
                    else if (meal_time == 'lunch') {
                        lunchSeries.push(data_point);
                    } else {
                        dinnerSeries.push(data_point);
                    }
                }
            });

        });

        $('.eating-info--graph').highcharts({
            rangeSelector: {
                selected: 1
            },
            chart: {
                type: "bar"
            },
            title: {
                text: "Eating Info"
            },
            yAxis: {
                title: {
                    text: "Calories"
                },
                lineWidth: 2
            },
            xAxis: {
                title: {
                    text: "Day"
                },
                categories: days_used
            },
            series: [
                {
                    type: 'bar',
                    name: 'Breakfast',
                    data: breakfastSeries
                },
                {
                    type: 'bar',
                    name: 'Lunch',
                    data: lunchSeries
                },
                {
                    type: 'bar',
                    name: 'Dinner',
                    data: dinnerSeries
                }],
            credits: {
                enabled: false
            }
        });
    }

    function show_exercise_info(json) {
        var series = [];

        var days_used = [];

        var records = json['records'];
        $.each(records, function (index, record) {
            var phys_info = record['physical_activity'];
            $.each(phys_info, function (index, phys) {
                var activity_type = phys.activity_type;
                var local_series;
                $.each(series, function(index, ser){
                    if('name' in ser && ser['name'] === activity_type){
                        local_series = ser;
                    }
                });
                if (!local_series || local_series ==  undefined) {
                    local_series = {
                        'name': activity_type,
                        'data': []
                    };
                    series.push(local_series);
                }
                var series_data = local_series.data;

                var data_point = [
                    record.activity_date,
                    phys.duration
                ];
                if (!record.activity_date in days_used )
                    days_used.push(record.activity_date);
                series_data.push(data_point);

            });

        });

        $('.phys-info--graph').highcharts({
            rangeSelector: {
                selected: 1
            },
            chart: {
                type: "bar"
            },
            title: {
                text: "Exercise History"
            },
            yAxis: {
                title: {
                    text: "Duration in minutes"
                },
                lineWidth: 2
            },
            xAxis: {
                title: {
                    text: "Day"
                },
                categories: days_used
            },
            series: series,
            credits: {
                enabled: false
            }
        });
    }
}