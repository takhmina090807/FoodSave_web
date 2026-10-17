import { useState } from 'react';
import { AlertTriangle, Check, Clock3, Plus, X } from 'lucide-react';
import { restaurants, type Meal } from './data';

const tiers=[{name:'Solo',price:18,value:36,detail:'A satisfying dinner for one'},{name:'Classic',price:25,value:50,detail:'A little extra to enjoy'},{name:'Share',price:32,value:64,detail:'Made for sharing'}];
const allergenOptions=['Gluten','Milk','Eggs','Peanuts','Tree nuts','Soy','Sesame','Fish','Shellfish'];

export default function SurpriseBoxModal({meal,close,add}:{meal:Meal;close:()=>void;add:(meal:Meal,avoid?:string[])=>void}){
 const [tier,setTier]=useState(0); const [avoid,setAvoid]=useState<string[]>([]); const selected=tiers[tier]; const partner=restaurants.find(r=>r.id===meal.restaurantId);
 const toggle=(allergen:string)=>setAvoid(current=>current.includes(allergen)?current.filter(x=>x!==allergen):[...current,allergen]);
 const addBox=()=>{add({...meal,id:`${meal.id}-${selected.price}-${avoid.map(x=>x.toLowerCase().replace(/ /g,'-')).sort().join('-')||'any'}`,price:selected.price,original:selected.value},avoid);close()};
 return <div className="overlay modal-overlay" onMouseDown={e=>{if(e.target===e.currentTarget)close()}}><article className="surprise-modal">
  <button className="modal-close icon-button" onClick={close} aria-label="Close dinner surprise box"><X/></button>
  <div className="surprise-modal-photo"><img src={meal.image} alt="A sample dinner dish"/><span className="demo-label">DEMO BOX</span></div>
  <div className="surprise-modal-content"><div className="eyebrow">A DELICIOUS LITTLE MYSTERY</div><h2>{meal.name}</h2><p className="surprise-byline">{partner?.name} · Demo partner</p><p>{meal.description}</p>
   <div className="surprise-modal-facts"><span><Clock3 size={14}/>Pickup {meal.pickup}</span><span>{meal.portions} demo boxes remaining</span></div>
   <fieldset className="box-tier-field"><legend>Choose your box size</legend>{tiers.map((option,index)=><label className={`box-tier ${tier===index?'box-tier-selected':''}`} key={option.name}><input type="radio" name="box-size" checked={tier===index} onChange={()=>setTier(index)}/><span className="tier-check">{tier===index&&<Check size={12}/>}</span><span className="tier-copy"><b>{option.name}</b><small>{option.detail}</small></span><span className="tier-price"><b>AED {option.price}</b><small>Est. value AED {option.value}</small></span></label>)}</fieldset>
   <fieldset className="allergen-field"><legend>Any allergens you need to avoid?</legend><p>Select all that apply. We’ll add this preference to your demo order.</p><div className="allergen-options">{allergenOptions.map(option=><label className={`allergen-option ${avoid.includes(option)?'allergen-option-selected':''}`} key={option}><input type="checkbox" checked={avoid.includes(option)} onChange={()=>toggle(option)}/><span>{option}</span></label>)}</div></fieldset>
   <div className="allergy-warning"><AlertTriangle size={17}/><p><b>Please check with the restaurant.</b> Surprise contents change daily. Your selections are preferences only and cannot guarantee an allergen-free box.</p></div>
   <button className="btn btn-primary surprise-add" onClick={addBox}>Add {selected.name.toLowerCase()} box · AED {selected.price}<Plus size={16}/></button>
   <small className="demo-note">Fresh surplus · exact dishes vary · no real payment is collected</small>
  </div>
 </article></div>
}
