#!/usr/bin/python3
# -*- coding: utf-8 -*-
#


##Copyright (c) 2018, Tarmo Tanilsoo
##All rights reserved.
##
##Redistribution and use in source and binary forms, with or without
##modification, are permitted provided that the following conditions are met:
##
##1. Redistributions of source code must retain the above copyright notice,
##this list of conditions and the following disclaimer.
##
##2. Redistributions in binary form must reproduce the above copyright notice,
##this list of conditions and the following disclaimer in the documentation
##and/or other materials provided with the distribution.
##
##3. Neither the name of the copyright holder nor the names of its contributors
##may be used to endorse or promote products derived from this software without
##specific prior written permission.
##
##THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
##AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
##IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
##ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
##LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
##CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
##SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
##INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
##CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
##ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##POSSIBILITY OF SUCH DAMAGE.
#

#Phrases for TRV software
#Estonian
import sys
phrases={"estonian":
         {
             "name":"TRV EX1-a",
             "loading_states":"Laen andmeid... Osariigid",
             "coastlines":"Rannajooned",
             "countries":"Maismaapiirid",
             "country_boundaries":"riigipiirid",
             "lakes":u"Järved",
             "rivers":u"Jõed",
             "placenames":"andmepunktid",
             "states_counties":"osariigid/maakonnad",
             "NA_roads":u"Põhja-Ameerika suured maanteed",
             "add_rmax":"Liida Rmax",
             "az0":"Algasimuut(°):",
             "az1":u"Lõppasimuut(°):",
             "r0":"Algkaugus(km):",
             "r1":u"Lõppkaugus(km):",
             "prf":"PRF(Hz):",
             "add":"Liida",
             "nexrad_choice":"NEXRAD jaama valik",
             "choose_station":"Vali jaam",
             "okbutton":"OK",
             "choose_station_error":"Palun vali jaam!",
             "open_url":"Ava fail internetist",
             "open":"Ava",
             "download_failed":u"Allalaadimine ebaõnnestus!",
             "hca_names":["Bioloogiline",
                   u"Anomaalne levi/pinnamüra",
                   u"Jääkristallid",
                   "Kuiv lumi",
                   u"Märg lumi",
                   "Vihm",
                   "Tugev vihm",
                   "Suured piisad",
                   "Lumekruubid",
                   "Rahe",
                   "Tundmatu",
                   "RF"],
             "iris_hca":["",
                         "Mittemeteoroloogiline",
                         "Vihm",
                         u"Märg lumi",
                         "Lumi",
                         "Lumekruubid",
                         "Rahe"],
             "level3_slice":u"Lõik /NR/",
             "export_success":"Eksport edukas",
             "export_format_fail":u"Valitud vormingusse ei saa salvestada või puudub asukohas kirjutamisõigus.",
             "no_data":"Andmed puuduvad",
             "about_text":"Tarmo Tanilsoo, 2018\ntarmotanilsoo@gmail.com\n\nPythoni versioon: "+sys.version,
             "key_shortcuts_dialog_text":u"Otseteed klaviatuuril:\n\nz - suurendamisrežiimi\np - ringiliikumisrežiimi\ni - infokogumiserežiimi\nr - algsuurendusse tagasi",
             "azimuth":"Asimuut",
             "range":"Kaugus",
             "value":u"Väärtus",
             "beam_height":u"Kiire kõrgus",
             "g2g_shear":"G2G nihe",
             "height":u"Kõrgus",
             "drawing":"Joonistan...",
             "radar_image":"radaripilt",
             "ready":"Valmis",
             "decoding":"Dekodeerin...",
             "incorrect_format":u"Viga: Tegemist ei ole õiges formaadis failiga", #Apparently none of supported formats
             "not_found_at_this_level":u"Sellel kõrgustasemel seda produkti ei leitud.",
             "error_during_loading":"Laadimisel juhtus viga",
             "choose_pseudorhi_status":"Kliki asimuudil, millest soovid PseudoRHI'd teha",
             "cant_make_pseudorhi":u"PseudoRHI'd ei ole nende andmetega võimalik teha",
             "reading_elevation":"Loen elevatsiooni: ",
             "drawing_pseudorhi":"Joonistan pseudoRHI'd",
             "file":"Fail",
             "nexrad":"NEXRAD Level 3",
             "tools":u"Tööriistad",
             "help":"Abi",
             "open_datafile":"Ava andmefail",
             "export_img":"Ekspordi pilt",
             "quit":u"Lõpeta",
             "current_data":"Jooksvad andmed",
             "level3_station_selection":"Jaama valik",
             "dealiasing":"Radiaalkiiruste dealiasing",
             "key_shortcuts_menuentry":"Otseteed klaviatuuril",
             "about_program":"Info programmi kohta",
             "th":u"täielik peegelduvus (h)",
             "tv":u"täielik peegelduvus (v)",
             "product_reflectivity":"peegelduvus",
             "dbzh":"peegelduvus (h)",
             "dbzv":"peegelduvus (v)", 
             "sqi":"signaalikvaliteedi indeks", 
             "product_radialvelocity":"radiaalkiirus",
             "vradh":"radiaalkiirus (h)",
             "vradv":"radiaalkiirus (v)",
             "vraddh":"dealiasitud radiaalkiirus (h)",
             "vraddv":"dealiasitud radiaalkiirus (v)",
             "product_rhohv":"korrelatsioonikoefitsent",
             "product_zdr":"diferentsiaalne peegelduvus",
             "product_kdp":"spetsiifiline diferentsiaalne faas",
             "product_hclass":u"hüdrometeoori klassifikatsioon",
             "product_sw":"spektrilaius",
             "wradh":"spektrilaius (h)",
             "wradv":"spektrilaius (v)",
             "product_phi":"diferentsiaalne faas",
             "qidx":"kvaliteet",
             "no_data_loaded":"Andmeid pole laetud!",
             "current_language":"Keel",
             "language_estonian":"Eesti keel",
             "language_english":"English",
             "conf_restart_required":u"Muutus aktiveerub programmi taaskäivitamisel.",
             "sweep":"viibe",
             "dyn_labels":u"Dünaamilised andmepunktid",
             "color_table":u"Värvitabeli vahetus",
             "default_colors":u"Vaikimisi värvid",
             "dyn_new":"Lisa",
             "dyn_edit":"Muuda",
             "dyn_rm":"Kustuta",
             "dyn_rm_sure":"Kindel, et soovid seda allikat kustutada?",
             "dyn_view":"Vaata",
             "dyn_online":"Internetis",
             "dyn_local":"Kohalik",
             "dyn_path":"Aadress:",
             "dyn_interval":"Miinimumvahe uuenduste vahel(min): ",
             "dyn_enabled":u"Sisse lülitatud",
             "batch_export":"Ekspordi hulgi",
             "batch_input":"Andmete kaust: ",
             "batch_output":u"Väljundi kaust: ",
             "batch_pick":"Vali kaust",
             "batch_fmt":u"Väljundi vorming",
             "batch_product":u"Produkt",
             "batch_el":"Kaldenurk",
             "batch_notfound":u"Päritud andmeid ei leitud sellel kõrgustasemel failis ",
             "batch_notfound2":"Eksport katkestatakse.",
             "batch_notfilled":u"Palun vaadake, et nii andmete kui ka väljundi kaust oleks määratud.",
             "ddp_error":u"Viga dünaamiliste andmepunktide failis: "
             },
         "english":
         {
             "name":"TRV EX1-a",
             "loading_states":"Loading data... States",
             "coastlines":"Coastlines",
             "countries":"Countries",
             "country_boundaries":"country boundaries",
             "lakes":"Lakes",
             "rivers":"Rivers",
             "placenames":"data points",
             "states_counties":"states/counties",
             "NA_roads":"Major North American highways",
             "add_rmax":"Add Rmax",
             "az0":"Initial azimuth(°):",
             "az1":"Final azimuth(°):",
             "r0":"Initial range(km):",
             "r1":u"Final range(km):",
             "prf":"PRF(Hz):",
             "add":"Add",
             "nexrad_choice":"NEXRAD station choice",
             "choose_station":"Choose a station",
             "okbutton":"OK",
             "choose_station_error":"Please choose a station!",
             "open_url":"Open an URL",
             "open":"Open",
             "download_failed":u"Download failed!",
             "hca_names":["Biological",
                   "Anomalous propagation/ground clutter",
                   u"Ice crystals",
                   "Dry snow",
                   u"Wet snow",
                   "Rain",
                   "Heavy rain",
                   "Large drops",
                   "Graupel",
                   "Hail",
                   "Unknown",
                   "RF"],
             "iris_hca":["",
                         "Non-meteorological",
                         "Rain",
                         "Wet snow",
                         "Snow",
                         "Graupel",
                         "Hail"],
             "level3_slice":u"Slice /NR/",
             "export_success":"Export successful",
             "export_format_fail":"Either unable to save into this format or lacking writing permissions at the destination.",
             "no_data":"No data",
             "about_text":"Tarmo Tanilsoo, 2018\ntarmotanilsoo@gmail.com\n\nPython version:"+sys.version,
             "key_shortcuts_dialog_text":u"Shortcuts on keyboard:\n\nz - zoom mode\np - panning mode\ni - data gathering mode\nr - reset zoom",
             "azimuth":"Azimuth",
             "range":"Range",
             "value":u"Value",
             "beam_height":u"Beam height",
             "g2g_shear":"G2G shear",
             "height":u"Height",
             "drawing":"Drawing...",
             "radar_image":"radar image",
             "ready":"Ready",
             "decoding":"Decoding...",
             "incorrect_format":u"Error. File is not in a supported format", #Apparently none of supported formats
             "not_found_at_this_level":u"Product not found at this elevation.",
             "error_during_loading":"Error during loading",
             "choose_pseudorhi_status":"Click at the desired azimuth to generate a pseudoRHI",
             "cant_make_pseudorhi":u"It is not possible to make a pseudoRHI using this data file",
             "reading_elevation":"Reading elevation: ",
             "drawing_pseudorhi":"Drawing a pseudoRHI",
             "file":"File",
             "nexrad":"NEXRAD Level 3",
             "tools":u"Tools",
             "help":"Help",
             "open_datafile":"Open data file",
             "export_img":"Export image",
             "quit":u"Quit",
             "current_data":"Current data",
             "level3_station_selection":"Station selection",
             "dealiasing":"Radial velocities dealiasing",
             "key_shortcuts_menuentry":"Keyboard shortcuts",
             "about_program":"About",
             "product_reflectivity":"reflectivity",
             "th":u"total reflectivity (h)",
             "tv":u"total reflectivity (v)",
             "dbzh":"reflectivity (h)",
             "dbzv":"reflectivity (v)", 
             "sqi":"signal quality index",
             "qidx":"quality",
             "product_radialvelocity":"radial velocity",
             "vradh":"radial velocity (h)",
             "vradv":"radial velocity (v)",
             "vraddh":"dealiased radial velocity (h)",
             "vraddv":"dealiased radial velocity (v)",
             "product_zdr":"differential reflectivity",
             "product_rhohv":"correlation coefficient",
             "product_kdp":"specific differential phase",
             "product_hclass":"hydrometeor classification",
             "product_sw":"spectrum width",
             "wradh":"spectrum width (h)",
             "wradv":"spectrum width (v)",
             "product_phi":"differential phase",
             "no_data_loaded":"No data loaded!",
             "current_language":"Language",
             "language_estonian":"Eesti keel",
             "language_english":"English",
             "conf_restart_required":"Change will take effect upon next startup.",
             "sweep":"sweep",
             "dyn_labels":"Dynamic data points",
             "color_table":"Color table override",
             "default_colors":"Default colors",
             "dyn_new":"Add",
             "dyn_edit":"Edit",
             "dyn_rm":"Delete",
             "dyn_rm_sure":"Are you sure you want to delete this entry?",
             "dyn_view":"View",
             "dyn_online":"Online",
             "dyn_local":"Local",
             "dyn_path":"Path:",
             "dyn_interval":"Minimum interval between updates(min):",
             "dyn_enabled":"Enabled",
             "batch_export":"Batch export",
             "batch_input":"Input directory: ",
             "batch_output":"Output directory: ",
             "batch_pick":"Pick a directory",
             "batch_fmt":"Output format",
             "batch_product":"Product",
             "batch_el":"Elevation",
             "batch_notfound":"Requested data not found at this elevation in file ",
             "batch_notfound2":"Export will be stopped.",
             "batch_notfilled":"Please ensure that input and output directories are both specified",
             "ddp_error":"Error in dynamic data point file: "
             }
    }
