import inspect

from redgifs import Tags as t

def __get_value(element: t | str) -> str:
    if (isinstance(element, t)): return element.value
    return element

# TODO: stop using tags_mapping
__RGTagMap: dict[str, list[t | str]] = {
    "airtight": [t.tags_mapping.get("double_penetration"), t.tags_mapping.get("blowjob")],
    "anal": [t.tags_mapping.get("anal")],
    "anal creampie": [t.tags_mapping.get("anal_creampie")],
    "anal fingering": [t.tags_mapping.get("anal"), t.tags_mapping.get("fingering")],
    "anal fisting": [t.tags_mapping.get("anal"), t.tags_mapping.get("fisting")],
    "anal gape": [t.tags_mapping.get("anal"), t.tags_mapping.get("gape"), t.tags_mapping.get("gaping")],
    "bbc": [t.tags_mapping.get("bbc")],
    "blowjob": [t.tags_mapping.get("blowjob")],
    "choking": [t.tags_mapping.get("choking")],
    "close up": [t.tags_mapping.get("close_up")],
    "cowgirl": [t.tags_mapping.get("cowgirl")],
    "cum in mouth": [t.tags_mapping.get("cum_in_mouth")],
    "dap": [t.tags_mapping.get("double_anal")],
    "deep throat": [t.tags_mapping.get("deepthroat")],
    "doggy": [t.tags_mapping.get("doggystyle")],
    "dp": [t.tags_mapping.get("double_penetration")],
    "dvp": [t.tags_mapping.get("double_vaginal")],
    "face fuck": [t.tags_mapping.get("face_fuck")],
    "facial": [t.tags_mapping.get("facial")],
    "fingering": [t.tags_mapping.get("fingering")],
    "fisting": [t.tags_mapping.get("fisting")],
    "full nelson": [t.tags_mapping.get("full_nelson")],
    "hair pulling": [t.tags_mapping.get("hair_pulling")],
    "piss": [t.tags_mapping.get("piss")],
    "prolapse": [t.tags_mapping.get("anal"), t.tags_mapping.get("gape")],
    "reverse cowgirl": [t.tags_mapping.get("reverse_cowgirl")],
    "side": [t.tags_mapping.get("side_fuck")],
    "spanking": [t.tags_mapping.get("spanking")],
    "squirting": [t.tags_mapping.get("squirt"), t.tags_mapping.get("squirting")],
    "standing": ["r/StandingCarryFuck"],
    "triple penetration": ["Triple Penetration"],
    "masturbation": [t.tags_mapping.get("masturbating")],
    "ass licking": [t.tags_mapping.get("licking"), t.tags_mapping.get("lick")],
    "anal dildo": [t.tags_mapping.get("anal"), t.tags_mapping.get("dildo")],
    "slapping": [t.tags_mapping.get("slapping")],
    "handjob": [t.tags_mapping.get("handjob")],

    "dildo": ["Dildo"],
    "blowbang": ["Blowbang"],
    "piss in mouth": ["Piss", "Pissing"],
    "triple anal": [t.tags_mapping.get("triple_penetration")],
    
    "Adriana Chechik": t.tags_mapping.get("adriana_chechik"),
    "Jane Wilde": t.tags_mapping.get("jane_wilde"),
    "Martina Smeraldi": t.tags_mapping.get("martina_smeraldi"),
    "Rebel Rhyder": "Rebel Rhyder",
    "Sara Bell": t.tags_mapping.get("sara_bell"),
    "Kyler Quinn": t.tags_mapping.get("kyler_quinn"),
    "Funky Town": "",
    "Ella Elastic": "",
    "Natalia Starr": t.tags_mapping.get("natalia_starr"),
    "Emily Pink": "",
    "Karolina Geiman": "",
}

RGTagMap: dict[str, list[str]] = {
    k: ([__get_value(value) for value in vals_or_val] if isinstance(vals_or_val, list) else __get_value(vals_or_val))
    for (k, vals_or_val) in __RGTagMap.items()}

# RGTagMap: dict[str, list[str]] = {
#     "airtight": [t.double_penetration.value, t.blowjob.value],
#     "anal": [t.anal.value],
#     "anal fingering": [t.anal.value, t.fingering.value],
#     "anal fisting": [t.anal.value, t.fisting.value],
#     "anal gape": [t.anal.value, t.gape.value, t.gaping.value],
#     "bbc": [t.bbc.value],
#     "blowjob": [t.blowjob.value],
#     "choking": [t.choking.value],
#     "close up": [t.close_up.value],
#     "cowgirl": [t.cowgirl.value],
#     "dap": [t.double_anal.value],
#     "deep throat": [t.deepthroat.value],
#     "doggy": [t.doggystyle.value],
#     "dp": [t.double_penetration.value],
#     "dvp": [t.double_vaginal.value],
#     "face fuck": [t.face_fuck.value],
#     "facial": [t.facial.value],
#     "fingering": [t.fingering.value],
#     "fisting": [t.fisting.value],
#     "full nelson": [t.full_nelson.value],
#     "hair pulling": [t.hair_pulling.value],
#     "prolapse": [t.anal.value, t.gape.value],
#     "reverse cowgirl": [t.reverse_cowgirl.value],
#     "side": [t.side_fuck.value],
#     "spanking": [t.spanking.value],
#     "squirting": [t.squirt.value, t.squirting.value],
#     "standing": ["r/StandingCarryFuck"],
#     "triple penetration": ["Triple Penetration"],
#     "masturbation": [t.masturbating.value],
#     "ass licking": [t.licking.value, t.lick.value],
#     "Adriana Chechik": t.adriana_chechik.value,
#     "Jane Wilde": t.jane_wilde.value,
#     "Martina Smeraldi": t.martina_smeraldi.value,
#     "Rebel Rhyder": "Rebel Rhyder",
#     "Sara Bell": t.sara_bell.value,
#     "Kyler Quinn": t.kyler_quinn.value
# }
