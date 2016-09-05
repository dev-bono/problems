'use strict';

angular.module('confusionApp', [])
    .controller('menuController', function(){

        this.tab = 1;
        this.filtText = '';

        var dished = [
                          {
                            name: 'Uthapizza',
                            image: 'images/uthapizza.png',
                            category: 'mains',
                            label: 'Hot',
                            price: '4.99',
                            description:'A unique combination of Indizan Uthappam (pancake) and Italian pizza, topped with Cerignola olives, ripe vine cherry tomatoes, Vidalia onion, Guntur chillies and Buffalo Paneer',
                            comment: 'aaaaaaa'
                          },
                          {
                            name: 'Uthapizza2',
                            image: 'images/zucchipakoda.png',
                            category: 'mains',
                            label: '',
                            price: '4.99',
                            description:'A unique combination of Indizan Uthappam (pancake) and Italian pizza, topped with Cerignola olives, ripe vine cherry tomatoes, Vidalia onion, Guntur chillies and Buffalo Paneer',
                            comment: ''
                          },
                          {
                            name: 'Uthapizza3',
                            image: 'images/vadonut.png',
                            category: 'appetizer',
                            label: 'New',
                            price: '4.99',
                            description:'A unique combination of Indizan Uthappam (pancake) and Italian pizza, topped with Cerignola olives, ripe vine cherry tomatoes, Vidalia onion, Guntur chillies and Buffalo Paneer',
                            comment: ''
                          },
                          {
                            name: 'Uthapizza4',
                            image: 'images/elaicheesecake.png',
                            category: 'dessert',
                            label: '',
                            price: '4.99',
                            description:'A unique combination of Indizan Uthappam (pancake) and Italian pizza, topped with Cerignola olives, ripe vine cherry tomatoes, Vidalia onion, Guntur chillies and Buffalo Paneer',
                            comment: ''
                          },
                        ];
        this.dishes = dished;

        this.select = function(setTab) {
            this.tab = setTab;

            if (setTab === 2) {
                this.filtText = "appetizer";
            } else if (setTab === 3) {
                this.filtText = "mains";
            } else if (setTab === 4) {
                this.filtText = "dessert";
            } else {
                this.filtText = "";
            }
        };

        this.isSelected = function(checkTab) {
            return (this.tab === checkTab);
        };
    });