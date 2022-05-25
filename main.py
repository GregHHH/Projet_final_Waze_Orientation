import streamlit as st
import time
import pandas as pd
import numpy as np

st.title("Rencontre les formations et métiers les plus chauds de ta région")
st.write(" L'Orientation à portée de mains. ")

# =============================================================================
# 				Functions related to the display of the results               #
# =============================================================================
def get_dataset(dataset_name):
	if dataset_name == 'Métier':
		v = None
		return v
	else:
		return None


def add_params(type):
	params = dict()
	if search_type == 'Métiers':	
		M = st.sidebar.text_input('Métier souhaité:')
		L = search_location = st.sidebar.selectbox('Position Géo:', ("None", 'Ain (01)', 'Aisne (02)', 'Allier (03)', 'Alpes-de-Haute-Provence (04)', 'Alpes-Maritimes (06)', 'Ardèche (07)', 'Ardennes (08)', 'Ariège (09)', 'Aube (10)', 'Aude (11)', 'Aveyron (12)', 'Bas-Rhin (67)', 'Bouches-du-Rhône (13)', 'Calvados (14)', 'Cantal (15)', 'Charente (16)', 'Charente-Maritime (17)', 'Cher (18)', 'Corrèze (19)', 'Corse-du-Sud (2A)','Côte-d\'Or (21)', 'Côtes-d\'Armor (22)', 'Creuse (23)', 'Deux-Sèvres (79)', 'Dordogne (24)', 'Doubs (25)', 'Drôme (26)', 'Essonne (91)','Eure (27)', 'Eure-et-Loir (28)', 'Finistère (29)', 'Gard (30)', 'Gers (32)', 'Gironde (33)', 'Guadeloupe (971)', 'Guyane (973)','Haut-Rhin (68)', 'Haute-Corse (2B)', 'Haute-Garonne (31)', 'Haute-Loire (43)', 'Haute-Marne (52)', 'Haute-Saône (70)', 'Haute-Savoie (74)','Haute-Vienne (87)', 'Hautes-Alpes (05)', 'Hautes-Pyrénées (65)', 'Hauts-de-Seine (92)', 'Hérault (34)', 'Ille-et-Vilaine (35)', 'Indre (36)', 'Indre-et-Loire (37)', 'Isère (38)', 'Jura (39)', 'La Réunion (974)', 'Landes (40)', 'Loir-et-Cher (41)','Loire (42)', 'Loire-Atlantique (44)', 'Loiret (45)', 'Lot (46)', 'Lot-et-Garonne (47)', 'Lozère (48)', 'Maine-et-Loire (49)', 'Manche (50)','Marne (51)', 'Martinique (972)', 'Mayenne (53)', 'Mayotte (976)', 'Meurthe-et-Moselle (54)', 'Meuse (55)', 'Morbihan (56)', 'Moselle (57)', 'Nièvre (58)', 'Nord (59)','Oise (60)', 'Orne (61)', 'Paris (75)', 'Pas-de-Calais (62)', 'Puy-de-Dôme (63)', 'Pyrénées-Atlantiques (64)', 'Pyrénées-Orientales (66)', 'Rhône (69)', 'Saône-et-Loire (71)', 'Sarthe (72)','Savoie (73)', 'Seine-et-Marne (77)', 'Seine-Maritime (76)','Seine-Saint-Denis (93)', 'Somme (80)', 'Tarn (81)', 'Tarn-et-Garonne (82)', 'Territoire de Belfort (90)', "Val-d'Oise (95)",'Val-de-Marne (94)', 'Var (83)', 'Vaucluse (84)', 'Vendée (85)', 'Vienne (86)', 'Vosges (88)', 'Yonne (89)', 'Yvelines (78)'))
		params["Métier"] = M
		params["Position Géo"] = L
		return params
	if search_type == 'Compétences':
		S = st.sidebar.text_input('Compétences souhaitées:', )
		params["Compétences"] = S
		L = search_location = st.sidebar.selectbox('Position Géo:', ("None", 'Ain (01)', 'Aisne (02)', 'Allier (03)', 'Alpes-de-Haute-Provence (04)', 'Alpes-Maritimes (06)', 'Ardèche (07)', 'Ardennes (08)', 'Ariège (09)', 'Aube (10)', 'Aude (11)', 'Aveyron (12)', 'Bas-Rhin (67)', 'Bouches-du-Rhône (13)', 'Calvados (14)', 'Cantal (15)', 'Charente (16)', 'Charente-Maritime (17)', 'Cher (18)', 'Corrèze (19)', 'Corse-du-Sud (2A)','Côte-d\'Or (21)', 'Côtes-d\'Armor (22)', 'Creuse (23)', 'Deux-Sèvres (79)', 'Dordogne (24)', 'Doubs (25)', 'Drôme (26)', 'Essonne (91)','Eure (27)', 'Eure-et-Loir (28)', 'Finistère (29)', 'Gard (30)', 'Gers (32)', 'Gironde (33)', 'Guadeloupe (971)', 'Guyane (973)','Haut-Rhin (68)', 'Haute-Corse (2B)', 'Haute-Garonne (31)', 'Haute-Loire (43)', 'Haute-Marne (52)', 'Haute-Saône (70)', 'Haute-Savoie (74)','Haute-Vienne (87)', 'Hautes-Alpes (05)', 'Hautes-Pyrénées (65)', 'Hauts-de-Seine (92)', 'Hérault (34)', 'Ille-et-Vilaine (35)', 'Indre (36)', 'Indre-et-Loire (37)', 'Isère (38)', 'Jura (39)', 'La Réunion (974)', 'Landes (40)', 'Loir-et-Cher (41)','Loire (42)', 'Loire-Atlantique (44)', 'Loiret (45)', 'Lot (46)', 'Lot-et-Garonne (47)', 'Lozère (48)', 'Maine-et-Loire (49)', 'Manche (50)','Marne (51)', 'Martinique (972)', 'Mayenne (53)', 'Mayotte (976)', 'Meurthe-et-Moselle (54)', 'Meuse (55)', 'Morbihan (56)', 'Moselle (57)', 'Nièvre (58)', 'Nord (59)','Oise (60)', 'Orne (61)', 'Paris (75)', 'Pas-de-Calais (62)', 'Puy-de-Dôme (63)', 'Pyrénées-Atlantiques (64)', 'Pyrénées-Orientales (66)', 'Rhône (69)', 'Saône-et-Loire (71)', 'Sarthe (72)','Savoie (73)', 'Seine-et-Marne (77)', 'Seine-Maritime (76)','Seine-Saint-Denis (93)', 'Somme (80)', 'Tarn (81)', 'Tarn-et-Garonne (82)', 'Territoire de Belfort (90)', "Val-d'Oise (95)",'Val-de-Marne (94)', 'Var (83)', 'Vaucluse (84)', 'Vendée (85)', 'Vienne (86)', 'Vosges (88)', 'Yonne (89)', 'Yvelines (78)'))
		params["Position Géo"] = L
		D = st.slider('Durée de la formation souhaitée', 0, 10, 1)
		params["Durée"] = D
		return params


def display_search_infos_jobs(params):
	if (params['Position Géo'] == "None" and params['Métier'] != ""):
		w = st.write('Tu recherches une formation en tant que: "', params["Métier"], '" sans prendre en compte la localisation de la formation')
		return w
	elif params['Position Géo'] != "None" and params['Métier'] == "":
		w = st.write('Tu recherches une formation  proche de:  "', params["Position Géo"], '" sans prendre en compte le type de formation préféré')
		return w
	elif params['Position Géo'] == "None" and params['Métier'] == "":
		w = st.write('Sélectionne un métier et une localisation pour rechercher une formation')
		return w
	else:
		w= st.write('Tu recherches une formation en tant que: "', params["Métier"], '" proche de "', params["Position Géo"], '"')
		return w


def display_search_infos_skills(params):
	if (params['Position Géo'] == "None" and params['Compétences'] != ""):
		w = st.write('Tu recherches un métier mettant à profit les compétences: "', params["Compétences"], '" sans prendre en compte la localisation de la formation')
		return w
	elif params['Position Géo'] != "None" and params['Compétences'] == "":
		w = st.write('Tu recherches un emploi proche de:  "', params["Position Géo"], '" sans prendre en compte le type de métiers préféré')
		return w
	elif params['Position Géo'] == "None" and params['Compétences'] == "":
		w = st.write('Sélectionne un Compétences et une localisation pour rechercher un métier')
		return w
	else:
		w= st.write('Tu recherches un métier mettant à profit les compétences: "', params["Compétences"], '" proche de "', params["Position Géo"], '"')
		return w


def display_coord(geoloc):
	df = pd.read_csv('data/coord_dpt.csv')
	df_search = df[df['departement'] == geoloc]
	return df_search[[ 'latitude', 'longitude']]

# =============================================================================
# 					Functions related to ML and API calls                     #
# =============================================================================



# =============================================================================
# 						Organisation of the sidebar							  #
# =============================================================================
# main elements of the sidebar
with st.sidebar.container():
	search_type = st.sidebar.selectbox('Rechercher par:', (" ","Métiers", "Compétences"))

# tertiary elements of the sidebarfurther options)
with st.sidebar.container():
	params = add_params(search_type)

# tertiary elements of the sidebar (search button)
with st.sidebar.container():
	recherche = st.button('Rechercher')

# =============================================================================
# 							Basic behavior of the app    					  #
# =============================================================================

if search_type == 'Métiers':
	display_search_infos_jobs(params)
elif search_type == 'Compétences':
	display_search_infos_skills(params)



if recherche:
	coordinates = display_coord(params["Position Géo"])
	st.write(coordinates)	


# create a function to get only the lines with the closest distance to the params['Position Géo'] input.
def get_closest_lines(df, params):
	if params['Position Géo'] == "None":
		return df
	else:
		df_closest = df.loc[df['Distance'] == df['Distance'].min()]
		return df_closest