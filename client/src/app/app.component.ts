import { Component } from '@angular/core';
import { ServiceService } from './service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Heroes';
  heroes=[];
  hero={};
  private _heroService: ServiceService;
  
  constructor(_heroService: ServiceService){
    this._heroService=_heroService;

  }
  ngOnInit( ){
    let observable= this._heroService.getAll();
    observable.subscribe(data=>{
      this.heroes= data['heroes']
    });
  }
  newHero(){
    let observable= this._heroService.create(this.hero);
    observable.subscribe(data =>{
      console.log(data)
      this.hero={};
      this.ngOnInit();
    })
  }
}
