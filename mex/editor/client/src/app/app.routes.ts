import { Routes } from "@angular/router";
import { Subpage } from "./subpage/subpage";

export const routes: Routes = [
  { component: Subpage, path: "subpage", data: { title: "Sub Page" } },
  { component: Subpage, path: "sub/subpage", data: { title: "EVEN MORE Sub Page" } },
];
