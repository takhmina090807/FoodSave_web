import { Clock3, MapPin, Plus, Truck, X } from 'lucide-react';
import { meals, type Meal, type Restaurant } from './data';

export default function RestaurantModal({restaurant,close,setSelected,add}:{restaurant:Restaurant;close:()=>void;setSelected:(m:Meal)=>void;add:(m:Meal)=>void}){
 const offers=meals.filter(m=>m.restaurantId===restaurant.id);
 return <div className="overlay modal-overlay" onMouseDown={e=>{if(e.target===e.currentTarget)close()}}><article className="restaurant-modal">
  <button className="modal-close icon-button" onClick={close} aria-label="Close restaurant details"><X/></button>
  <img className="restaurant-modal-image" src={restaurant.image} alt={restaurant.name}/>
  <div className="restaurant-modal-main"><div className="eyebrow">FOODSAVE DEMO PARTNER · {restaurant.kind.toUpperCase()}</div><h2>{restaurant.name}</h2><p>{restaurant.description}</p>
   <div className="restaurant-detail-facts"><span><MapPin size={15}/>{restaurant.area}</span><span><Clock3 size={15}/>{restaurant.hours}</span><span><Truck size={15}/>Pickup and delivery options shown at demo checkout</span></div>
   <div className="restaurant-meals-head"><div><div className="eyebrow">FRESH FINDS</div><h3>Available meals</h3></div><span>{offers.length} demo offers</span></div>
   <div className="restaurant-offers">{offers.map(m=><div className="restaurant-offer" key={m.id}><img src={m.image} alt=""/><button className="restaurant-offer-name" onClick={()=>setSelected(m)}><b>{m.name}</b><small>{m.category} · {m.portions} portions · Pickup {m.pickup}</small></button><strong>AED {m.price}</strong><button className="add-button" aria-label={m.category==="Surprise box"?`Choose ${m.name} options`:`Add ${m.name}`} onClick={()=>m.category==="Surprise box"?setSelected(m):add(m)}><Plus size={16}/></button></div>)}</div>
   <small className="demo-note">Fictional partner and availability · demo address · while supplies last</small>
  </div>
 </article></div>
}
